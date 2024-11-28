# Scenes

To manage data in

```bash
data\scenes.json
```

Here’s a Python data model using `pydantic` and `dataclasses` that you can use to manage CRUD operations for your data. These classes will allow easy parsing, validation, and manipulation of your data structure.

### Pydantic Model for Validation and CRUD Operations

```python
from typing import List, Optional
from pydantic import BaseModel

# Define the Component model
class Component(BaseModel):
    name: str

# Define the System model
class System(BaseModel):
    name: str

# Define the Entity model
class Entity(BaseModel):
    name: str
    components: List[str]
    systems: List[str]

# Define the Scene model
class Scene(BaseModel):
    path: str
    name: str
    description: str
    image: Optional[str]
    entities: List[Entity]

# CRUD Operations Manager
class SceneManager:
    def __init__(self, scenes: Optional[List[Scene]] = None):
        self.scenes = scenes or []

    def create_scene(self, scene_data: dict):
        """Create a new scene."""
        scene = Scene(**scene_data)
        self.scenes.append(scene)

    def read_scene(self, name: str) -> Optional[Scene]:
        """Read a scene by name."""
        return next((scene for scene in self.scenes if scene.name == name), None)

    def update_scene(self, name: str, updated_data: dict) -> Optional[Scene]:
        """Update an existing scene."""
        scene = self.read_scene(name)
        if scene:
            for key, value in updated_data.items():
                setattr(scene, key, value)
        return scene

    def delete_scene(self, name: str) -> bool:
        """Delete a scene by name."""
        scene = self.read_scene(name)
        if scene:
            self.scenes.remove(scene)
            return True
        return False

    def list_scenes(self) -> List[Scene]:
        """List all scenes."""
        return self.scenes
```

### Example Usage

```python
# Example data
example_data = [
    {
        "path": "feature\\engine\\renderer\\canvas_scaling",
        "name": "canvas_scaling",
        "description": "Scene for testing feature of canvas content resizing.",
        "image": "-",
        "entities": [
            {
                "name": "canvas",
                "components": ["canvasScale"],
                "systems": ["canvasScaler", "contentScalerTester"]
            }
        ]
    }
]

# Initialize SceneManager with data
manager = SceneManager([Scene(**data) for data in example_data])

# Create a new scene
manager.create_scene({
    "path": "feature\\engine\\renderer\\new_feature",
    "name": "new_feature",
    "description": "Scene for testing a new feature.",
    "image": None,
    "entities": [
        {
            "name": "newEntity",
            "components": ["component1", "component2"],
            "systems": ["system1"]
        }
    ]
})

# Read a scene
scene = manager.read_scene("canvas_scaling")
print(scene)

# Update a scene
updated_scene = manager.update_scene("canvas_scaling", {"description": "Updated description for the scene."})
print(updated_scene)

# Delete a scene
deleted = manager.delete_scene("canvas_scaling")
print(f"Deleted: {deleted}")

# List all scenes
print(manager.list_scenes())
```

### Features

- **Create**: Add a new scene with `create_scene`.
- **Read**: Retrieve a scene by name with `read_scene`.
- **Update**: Modify an existing scene with `update_scene`.
- **Delete**: Remove a scene with `delete_scene`.
- **List**: View all scenes with `list_scenes`.

This data model and `SceneManager` class are ready for further integration with file storage, APIs, or UI components for CRUD operations.
