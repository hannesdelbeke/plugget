# we find multiple macro or maxscripts
# run them
# TODO polish: install to a custom location, env var, so user can overwrite default install location

# refresh the script paths
# a = getDir #userMacros
# macros.load(a)


def install(package: "plugget.data.Package") -> bool:  # todo , force=False, enable=True):
    # copy to macroscript folder
    # run maxscript

    pass
    # """install plugin from path"""
    # # If the “overwrite” parameter is True, the add-on will be reinstalled, even if it has not been previously removed.
    #
    # # manifest is named io_xray
    # # but subdir is io_scene_xray
    # # resulting in clashes. we cant just rename the subdir, might break code inside.
    # # so we need to track the "name" with plugin_name in the manifest
    #
    # # todo fix only support 1 plugin
    # plugin_path = plugin_paths[0]
    # if len(plugin_paths) > 1:
    #     raise NotImplemented("Only 1 plugin can be installed at a time for now")
    #
    # local_script_dir = bpy.utils.script_path_user()
    # local_addons_dir = Path(local_script_dir) / "addons"
    # new_plugin_path = local_addons_dir / plugin_path.name
    # shutil.move(str(plugin_path), str(new_plugin_path.parent))  # copy plugin_path to local_addons_dir
    #
    # # check if plugin folder was copied, by checking if any files are in new_plugin_path
    # if not any(new_plugin_path.iterdir()):
    #     logging.warning(f"Failed to install plugin {plugin_path.name}")
    #     return False
    # else:
    #     return True


def uninstall(name):
    # """uninstall plugin by name"""
    # if not name:
    #     logging.warning("No plugin name given")
    #     return
    # bpy.ops.preferences.addon_remove(module=name)