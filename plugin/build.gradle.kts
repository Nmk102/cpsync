import org.jetbrains.intellij.platform.gradle.IntelliJPlatformType
import org.jetbrains.kotlin.gradle.dsl.JvmDefaultMode
import org.jetbrains.kotlin.gradle.dsl.KotlinVersion

plugins {
    id("java")
    id("org.jetbrains.kotlin.jvm") version "2.3.21"
    id("org.jetbrains.intellij.platform") version "2.19.0"
}

group = "dev.cpsync"
version = "2.0.0"

repositories {
    mavenCentral()
    intellijPlatform {
        defaultRepositories()
    }
}

dependencies {
    testImplementation("junit:junit:4.13.2")
    testImplementation("org.opentest4j:opentest4j:1.3.0")
    intellijPlatform {
        // Используем только общие API платформы, поэтому собираем против IntelliJ Community,
        // а плагин работает в CLion (и любых других IDE JetBrains) 2025.1+.
        intellijIdeaCommunity("2025.1.7")
        pluginVerifier()
    }
}

intellijPlatform {
    pluginConfiguration {
        ideaVersion {
            sinceBuild = "251"
            untilBuild = provider { null }
        }
    }
    pluginVerification {
        ides {
            // проверка совместимости с реальным CLion: ./gradlew verifyPlugin
            create(IntelliJPlatformType.CLion, "2025.1.7")
            create(IntelliJPlatformType.CLion, "2026.2.4")
        }
    }
    buildSearchableOptions = false
    instrumentCode = false
}

kotlin {
    jvmToolchain(21)
    compilerOptions {
        // IDE 2025.1 содержит Kotlin stdlib 2.1 — не используем API новее
        apiVersion.set(KotlinVersion.KOTLIN_2_1)
        languageVersion.set(KotlinVersion.KOTLIN_2_1)
        // не генерировать переопределения default-методов интерфейсов платформы
        jvmDefault.set(JvmDefaultMode.NO_COMPATIBILITY)
    }
}

// Для отладки в песочнице (./gradlew runIde): без диалогов первого запуска
tasks.named<org.jetbrains.intellij.platform.gradle.tasks.RunIdeTask>("runIde") {
    jvmArgs(
        "-Didea.trust.all.projects=true",
        "-Djb.consents.confirmation.enabled=false",
        "-Didea.initially.ask.config=never",
        "-Djb.privacy.policy.text=<!--999.999-->",
    )
    System.getenv("CPSYNC_DEV_TOKEN")?.let { jvmArgs("-Dcpsync.token=$it") }
}
