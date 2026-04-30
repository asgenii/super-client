import src.cli.kernel as kernel
import src.cli.shell as shell
import src.core.loader as loader
import src.core.executor as executor
import src.core.replacer as replacer

Shell = shell.Shell("super#")
Loader = loader.Loader("commands/")
Executor = executor.Executor("commands/")
Replacer = replacer.Replacer("plugins/")

Kernel = kernel.Kernel(Shell, Loader, Executor, Replacer)
Kernel.run()