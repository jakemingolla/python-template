from .config.main import config


def main() -> None:
    print("Hello from python-template!")
    print(f"The default model is {config.default_model}.")


if __name__ == "__main__":
    main()
