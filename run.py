import src.cli.kernel as kernel
import src.cli.shell as shell
import src.core.loader as loader
import src.core.executor as executor

Shell = shell.Shell("super#")
Loader = loader.Loader("commands/")
Executor = executor.Executor("commands/")

Kernel = kernel.Kernel(Shell, Loader, Executor)
Kernel.run()