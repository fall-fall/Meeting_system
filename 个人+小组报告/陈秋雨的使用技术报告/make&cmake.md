# make 和 cmake 使用技术学习报告

**姓名:** 陈秋雨
**学号:** 2023302071273
**日期:** 2025年05月26日

---

## 目录

1. [make 和 cmake 是什么？](#1-make-和-cmake-是什么)
   * [1.1 make 是什么？](#11-make-是什么)
   * [1.2 cmake 是什么？](#12-cmake-是什么)
2. [基本工作原理简介](#2-基本工作原理简介)
   * [2.1 make 的工作原理](#21-make-的工作原理)
   * [2.2 cmake 的工作原理](#22-cmake-的工作原理)
3. [make 和 cmake 常规使用操作](#3-make-和-cmake-常规使用操作)
   * [3.1 make 的基本使用](#31-make-的基本使用)
   * [3.2 cmake 的基本使用](#32-cmake-的基本使用)
4. [学习总结](#4-学习总结)

---

## 1. make 和 cmake 是什么？

### 1.1 make 是什么？

**make** 是一个经典的构建自动化工具，主要用于从源代码自动生成可执行程序和库。它通过读取名为 `Makefile`（或 `makefile`）的文件来工作，该文件定义了项目的构建规则、文件间的依赖关系以及执行编译链接等任务所需的命令。

**主要目的和作用：**

* **自动化构建：** 根据 `Makefile` 中的指令自动执行编译、链接等步骤。
* **增量编译：** `make` 能够检查文件的时间戳，仅重新编译那些自上次编译以来已更改的源文件及其依赖文件，从而大大提高构建效率。
* **管理依赖：** 明确项目组件之间的依赖关系，确保以正确的顺序构建它们。

### 1.2 cmake 是什么？

**CMake** (Cross-platform Make) 是一个开源的、跨平台的构建系统生成器。它本身并不直接编译源代码，而是通过读取名为 `CMakeLists.txt` 的项目配置文件，根据当前操作系统和编译器环境，*生成*对应平台和工具链的本地构建文件（例如：Unix 平台下的 Makefiles，Windows 平台下的 Visual Studio 项目文件，macOS 平台下的 Xcode 项目文件等）。

**主要目的和作用：**

* **跨平台构建：** 开发者只需编写一套 `CMakeLists.txt` 文件，就可以在不同的操作系统和编译器上生成相应的构建环境。
* **管理复杂项目：** 更易于管理大型项目，支持模块化、外部库的查找与链接。
* **编译器和IDE无关性：** `CMakeLists.txt` 专注于描述项目的逻辑结构和构建需求，而不是特定编译器的命令。
* **支持核外构建 (Out-of-source builds)：** 允许将编译生成的文件与源代码文件分离开，保持源代码目录的整洁。

**为什么使用 CMake (相比直接编写 Makefile)：** 对于需要跨平台、或者项目结构较为复杂的情况，CMake 提供了更好的可移植性和可维护性。

---

## 2. 基本工作原理简介

### 2.1 make 的工作原理

* **Makefile 文件：** `make` 的核心是 `Makefile`。这个文件包含了一系列的**规则 (rules)**。每条规则通常包含：

  * **目标 (Target):** 通常是最终要生成的文件名（如可执行文件或目标文件），也可以是一个抽象的动作名（如 `clean`）。
  * **依赖 (Prerequisites/Dependencies):** 构建目标所需要的文件或其他目标。
  * **命令 (Commands):** 构建目标所需要执行的 Shell 命令（必须以 Tab 键开头）。

  ```makefile
  # 示例规则
  myprogram: main.o utils.o
      gcc -o myprogram main.o utils.o

  main.o: main.c utils.h
      gcc -c main.c -o main.o

  utils.o: utils.c utils.h
      gcc -c utils.c -o utils.o
  ```
* **依赖图 (Dependency Graph)：** `make` 会根据 `Makefile` 中的规则解析出一个依赖关系图。它从最终目标开始，递归地检查其依赖项，直到找到没有依赖或是依赖项已经是最新状态的项。
* **时间戳检查：** `make` 通过比较目标文件和其依赖文件的最后修改时间来决定是否需要重新执行命令。如果任何一个依赖文件比目标文件新，或者目标文件不存在，`make` 就会执行相应的命令来重新生成目标。

### 2.2 cmake 的工作原理

CMake 的工作过程通常分为两个主要阶段：

1. **配置 (Configure) 阶段：**

   * CMake 读取项目根目录下的 `CMakeLists.txt` 文件。
   * 它会检测当前的操作系统、编译器类型和版本等系统环境。
   * 处理 `CMakeLists.txt` 中的指令，例如查找库、设置编译选项等。
   * 根据检测到的环境和 `CMakeLists.txt` 的内容，生成本地构建系统所需的配置文件（例如 Makefiles 或 Visual Studio solution files）。这些文件会被放置在构建目录中。
   * 此阶段还会生成一个 `CMakeCache.txt` 文件，用于存储配置选项和检测结果，以便后续运行 CMake 时可以更快地加载配置。
2. **生成 (Generate) / 构建 (Build) 阶段：**

   * **生成阶段**是配置阶段的最终产物，即本地构建文件的创建。
   * **构建阶段**则是用户使用上一步生成的本地构建工具（如 `make`, `ninja`, Visual Studio IDE, Xcode）来实际编译和链接项目。CMake 本身也可以通过 `cmake --build .` 命令来自动调用底层的构建工具。

* **`CMakeLists.txt` 文件：** 这是 CMake 的输入文件，使用 CMake 特定的脚本语言编写。它描述了项目的源文件、目标（可执行文件、库）、依赖关系、编译选项等。
* **生成器 (Generators)：** CMake 使用生成器的概念来支持不同的本地构建系统。例如，`Unix Makefiles` 生成器会生成 Makefiles，`Visual Studio 16 2019` 生成器会生成 VS2019 的项目文件。

---

## 3. make 和 cmake 常规使用操作

### 3.1 make 的基本使用

#### 编写简单的 Makefile

一个基础的 Makefile 可能包含：

* **变量定义：** 用于存储编译器、编译选项等。
  ```makefile
  CC = gcc
  CFLAGS = -Wall -g
  TARGET = my_app
  OBJS = main.o helper.o
  ```
* **规则：**
  ```makefile
  # 第一个目标是默认目标
  all: $(TARGET)

  $(TARGET): $(OBJS)
      $(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

  main.o: main.c helper.h
      $(CC) $(CFLAGS) -c main.c -o main.o

  helper.o: helper.c helper.h
      $(CC) $(CFLAGS) -c helper.c -o helper.o

  # .PHONY 用于声明伪目标，这些目标不代表实际文件
  .PHONY: clean all

  clean:
      rm -f $(TARGET) $(OBJS)
  ```

#### 运行 make

* **`make`** 或 **`make all`**
  * 作用：执行 `Makefile` 中的第一个规则，或者名为 `all` 的规则（如果存在）。
* **`make [目标名]`**
  * 作用：构建指定的目标。
  * 示例：`make main.o`
* **`make clean`**
  * 作用：执行名为 `clean` 的规则，通常用于删除编译生成的文件。

### 3.2 cmake 的基本使用

#### 编写简单的 `CMakeLists.txt`

一个基础的 `CMakeLists.txt` 文件：

```cmake
# 1. 设置 CMake 最低版本要求
cmake_minimum_required(VERSION 3.10)

# 2. 定义项目名称
project(MyAwesomeProject LANGUAGES CXX) # 可以指定语言，如 C CXX

# 3. 添加可执行文件目标
# add_executable(<目标名> <源文件1> [源文件2 ...])
add_executable(my_app main.cpp utils.cpp)

# (可选) 添加库目标
# add_library(my_lib STATIC utils.cpp) # STATIC, SHARED, MODULE

# 4. (可选) 设置头文件包含目录
# target_include_directories(<目标名> PUBLIC|PRIVATE|INTERFACE <目录1> [目录2 ...])
target_include_directories(my_app PUBLIC "<span class="math-inline">\{CMAKE\_CURRENT\_SOURCE\_DIR\}/include"\)
\# 5\. \(可选\) 链接库
\# target\_link\_libraries\(<目标名\> PUBLIC\|PRIVATE\|INTERFACE <库名1\> \[库名2 \.\.\.\]\)
\# target\_link\_libraries\(my\_app PRIVATE my\_lib\) \# 如果 my\_lib 是本项目定义的库
\# target\_link\_libraries\(my\_app PRIVATE some\_external\_lib\) \# 链接外部库
\# 6\. \(可选\) 设置编译选项
\# target\_compile\_features\(my\_app PUBLIC cxx\_std\_17\) \# 要求 C\+\+17
\# set\(CMAKE\_CXX\_FLAGS "</span>{CMAKE_CXX_FLAGS} -Wall") # 添加编译警告

# (可选) 安装规则
# install(TARGETS my_app DESTINATION bin)
# install(FILES myheader.h DESTINATION include)
```
