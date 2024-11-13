tasks.register<Exec>("runApp") {
    group = "application"
    description = "Run the Python MVC app"
    commandLine("python3", "main.py")
}

tasks.register<Exec>("testApp") {
    group = "verification"
    description = "Run Python unit tests"
    commandLine("python3", "-m", "unittest", "discover", "-s", "tests")
}

tasks.register("build") {
    group = "build"
    description = "Custom build task that depends on tests"
    dependsOn("testApp")
}

tasks.register("clean") {
    group = "build"
    description = "Custom clean task to delete build directories"
    doLast {
        delete("build")
    }
}
