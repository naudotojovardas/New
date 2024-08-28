from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    testSMTP_SERVER: str
    testEMAIL_PORT: int
    testEMAIL_HOST_USER: str
    testEMAIL_HOST_PASSWORD: str

    class Config:
        env_file = "testing.env"


def send_mock_email(settings: Settings):
    print(f"testSMTP_SERVER: {settings.testSMTP_SERVER}")
    print(f"testEMAIL_PORT: {settings.testEMAIL_PORT}")
    print(f"testEMAIL_HOST_USER: {settings.testEMAIL_HOST_USER}")
    print(f"testEMAIL_HOST_PASSWORD: {settings.testEMAIL_HOST_PASSWORD}")
    # Mock email sending logic
    print("Pretending to send an email...")


if __name__ == "__main__":
    settings = Settings()
    send_mock_email(settings)