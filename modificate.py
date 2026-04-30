
import src.models.command as command
command = command.Command("src/cli/internal/commands")

# command.add({
#     "catalog": "",
#     "general": "",
#     "additional": [],
#     "description": "",
# })

command.build({
    "catalog": "exit",
    "general": "exit",
    "additional": [],
    "description": "shuts scripts down",
})

#################################################
# import src.models.plugin as plugin
# plugin = plugin.Plugin("plugins/")

# # plugin.build({
# #     "catalog": "",
# #     "general": "",
# #     "description": "",
# # })