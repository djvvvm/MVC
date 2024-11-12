tasks.register<Exec>("runApp") {
    group = "application"
    description = "Run the Python MVC app"
    commandLine("python3", "main.py")
}

tasks.register<Exec>("testApp") {
    group = "verification"
    description = "Run Python unit tests"
    commandLine("python", "-m", "unittest", "discover", "-s", "tests")
}