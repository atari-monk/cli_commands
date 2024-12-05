import json
from shared.cli_command import CLICommand
from shared.command import Command
from scene.model import Entity
from shared.constants import APP_NAME
from shared.logger_config import create_loggers
from keyval_storage.config_and_key_value_storage_data_model import ConfigAndKeyValueStorageDataModel
from shared.storage_key import StorageKey

class WriteCommand:
    def __init__(self):
        self.__file_path = ConfigAndKeyValueStorageDataModel(APP_NAME).getKeyValueStorage_LoadUsingConfig().get(StorageKey.SCENE_FILE_PATH.value)

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
        scene_data = self._collect_scene_data(parsed_args)
        self._add_entities_to_scene(scene_data)
        self._save_scene_to_file(scene_data)
        self.__log_final_scene_data(scene_data)
        self.__cliAndFileLogger.info(f"Scene '{scene_data['name']}' saved to {self.__file_path} and scenes.log.")

    def _collect_scene_data(self, parsed_args):
        name = parsed_args.name or input("Enter scene name: ").strip()
        path = parsed_args.path or input("Enter scene file path: ").strip()
        description = parsed_args.description or input("Enter scene description: ").strip()
        image = parsed_args.image or input("Enter optional image path (or leave blank): ").strip()

        return {
            "name": name,
            "description": description,
            "path": path,
            "image": image if image else None,
            "entities": []
        }

    def _save_scene_to_file(self, scene_data):
        try:
            with open(self.__file_path, 'a') as file:
                file.write(json.dumps(scene_data) + '\n')
            return True
        except Exception as e:
            self.__cliLogger.exception(f"Error appending scene data to file: {e}")
            return False

    def _add_entities_to_scene(self, scene_data):
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
                scene_data['entities'].append(entity.model_dump())
                self.__cliLogger.info(f"Entity '{entity_name}' added to scene '{scene_data['name']}'.")
            except Exception as e:
                self.__cliLogger.exception(f"Error creating entity: {e}")
                continue

            add_another = input("Add another entity? (y/n): ").strip().lower()
            if add_another != 'y':
                break

    def __log_final_scene_data(self, scene_data):
        self.__cliAndFileLogger.info(json.dumps(scene_data, indent=2))
        self.__cliLogger.info("\nScene data has been logged and appended successfully!")
