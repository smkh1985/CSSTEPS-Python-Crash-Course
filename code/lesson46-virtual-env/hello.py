from rich import print
from rich.console import Console

print("[bold magenta]Hello[/bold magenta] [green]World[/green]! :tada:")

console = Console()
console.print("[red]Error:[/red] Something went wrong.", style="blink")
