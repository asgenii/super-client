
import src.models.command as command
command = command.Command("temp/")

# command.add({
#     "catalog": "",
#     "general": "",
#     "additional": [],
#     "description": "",
# })

command.build({
    "catalog": "hw",
    "general": "hw",
    "additional": [],
    "description": "hw",
})

#################################################
# import src.models.plugin as plugin
# plugin = plugin.Plugin("plugins/")

# # plugin.build({
# #     "catalog": "",
# #     "general": "",
# #     "description": "",
# # })