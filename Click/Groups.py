import click


@click.group()
@click.option('--o', help='Some group option')
def main(o):
    print(o) if o else print('No group option')


@main.command()
@click.pass_context
@click.option('--co', help='Some command option')
def main_command1(ctx, co):
    print(co) if co else print('No command option')


if __name__ == "__main__":
    main()
