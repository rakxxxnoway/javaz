# ☕ javaz

A small CLI tool for setting up Java, Gradle and C++ projects.

---

## 📥 Installation

```bash
git clone https://github.com/rakxxxnoway/javaz.git
cd javaz
chmod 770 install.sh && ./install.sh
```

---

## 🚀 Usage

```
javaz <command> [language] <project_name> [flags]
```

---

## ⚙️ Commands

### ☕ `create java`

```bash
javaz create java <n> [--main | --empty]
```

`--main` / `-m` — generate project with `main.Main` entry point  
`--empty` / `-e` — only required dirs and files

---

### 🐘 `create gradle`

```bash
javaz create gradle <n> [--all] [--type TYPE] [--dsl DSL] [--pkg PKG]
```

`--all` — default setup (`java-application`, kotlin DSL, package `main`)  
`--dsl` — `kotlin` or `groovy`  
`--pkg` / `-p` — package name

`--type` / `-t` — one of: `basic`, `cpp-application`, `cpp-library`, `groovy-application`, `groovy-gradle-plugin`, `java-application`, `java-gradle-plugin`, `java-library`, `kotlin-application`, `kotlin-gradle-plugin`, `kotlin-library`, `pom`, `scala-application`, `scala-library`, `swift-application`, `swift-library`

---

### 🔧 `create c++`

```bash
javaz create c++ <n> [--make TARGET] [--include-local]
```

`--make` — generate a `Makefile` with given target  
`--include-local` — copy local `.cpp`/`.hpp` STD library

---

### 🗑️ `remove`

```bash
javaz remove <n>
```

---

## 📋 Dependencies

- Linux or macOS
- Python 3.10+
- `gradle` — for gradle projects
- `make` — for C++ projects with Makefile