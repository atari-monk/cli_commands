import json
import os
from shared.cli_command import CLICommand
from shared.command import Command
from scene.model import Entity
from shared.logger_config import create_loggers

class WriteCommand:
    def __init__(self):
        self.__cliLogger, self.__cliAndFileLogger = create_loggers("scenes", "scene_write")
        
        self.__cli_command = CLICommand(
            prog=Command.scene_write.cmd_name,
            description=Command.scene_write.desc
        )

        self.__cli_command.parser.add_argument('--name', type=str, help="Scene name.")
        self.__cli_command.parser.add_argument('--path', type=str, help="Scene file path.")
        self.__cli_command.parser.add_argument('--description', type=str, help="Scene description.")
        self.__cli_command.parser.add_argument('--image', type=str, help="Optional image for the scene.")

        self.__cli_command.set_execution_callback(self._execute_command)

    def run(self, input_args: str):
        self.__cli_command.parse_and_execute(input_args)

    def _execute_command(self, parsed_args):
        name = parsed_args.name or input("Enter scene name: ").strip()
        path = parsed_args.path or input("Enter scene file path: ").strip()
        description = parsed_args.description or input("Enter scene description: ").strip()

        image = parsed_args.image or input("Enter optional image path (or leave blank): ").strip()

        new_scene_data = {
            "name": name,
            "description": description,
            "path": path,
            "image": image if image else None,
            "entities": []
        }

        scenes = []
        if os.path.exists(path):
            try:
                with open(path, 'r') as file:
                    scenes = json.load(file)
                    if not isinstance(scenes, list):
                        raise ValueError("The file does not contain a valid list of scenes.")
            except Exception as e:
                print(f"Error loading existing scenes from file: {e}")
                return

        scenes.append(new_scene_data)

        try:
            with open(path, 'w') as file:
                json.dump(scenes, file, indent=2)
            print(f"New scene '{name}' appended to {path}.")
        except Exception as e:
            print(f"Error saving updated scene data: {e}")
            return

        while True:
            print("\nAdding a new entity:")
            entity_name = input("  Enter entity name: ").strip()
            components = input("  Enter components (comma-separated): ").strip().split(',')
            systems = input("  Enter systems (comma-separated): ").strip().split(',')

            try:
                entity = Entity(
                    name=entity_name,
                    components=[comp.strip() for comp in components if comp.strip()],
                    systems=[sys.strip() for sys in systems if sys.strip()]
                )
                new_scene_data['entities'].append(entity.model_dump())

                with open(path, 'w') as file:
                    json.dump(scenes, file, indent=2)
                print(f"Entity '{entity_name}' added to scene '{name}' and file updated.")
            except Exception as e:
                print(f"Error creating or saving entity: {e}")
                continue

            add_another = input("Add another entity? (y/n): ").strip().lower()
            if add_another != 'y':
                break

        self.__cliLogger.info(f"Final scene data: {new_scene_data}")
        self.__cliAndFileLogger.info(json.dumps(new_scene_data, indent=2))

        print("\nScene data has been logged and appended successfully!")
