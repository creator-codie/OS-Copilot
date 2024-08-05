from oscopilot import (
    FridayAgent,
    FridayExecutor,
    FridayPlanner,
    FridayRetriever,
    ToolManager,
)
from oscopilot.utils import setup_config, setup_pre_run

args = setup_config()
if not args.query:
    args.query = "Copy any text file located in the working_dir/document directory that contains the word 'agent' to a new folder named 'agents' "
task = setup_pre_run(args)
agent = FridayAgent(
    FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args
)
agent.run(task=task)
