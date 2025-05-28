# make 和 cmake 使用技术学习报告

**姓名:** 陈秋雨
**学号:** 2023302071273
**日期:** 2025年05月28日

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

# (可选) 添加库目标 (如果您的项目包含库)
# add_library(my_lib STATIC utils_lib.cpp) # 创建一个名为 my_lib 的静态库
# add_library(my_shared_lib SHARED shared_utils.cpp) # 创建一个共享库

# 4. (可选) 设置头文件包含目录
# target_include_directories(<目标名> PUBLIC|PRIVATE|INTERFACE <目录1> [目录2 ...])
target_include_directories(my_app PUBLIC "<span class="math-inline">\{CMAKE\_CURRENT\_SOURCE\_DIR\}/include"\)
\# 如果定义了 my\_lib，可能也需要为它指定头文件目录或让 my\_app 继承
\# if\(TARGET my\_lib\)
\#   target\_include\_directories\(my\_lib INTERFACE "</span>{CMAKE_CURRENT_SOURCE_DIR}/include")
# endif()

# 5. (可选) 链接库
# target_link_libraries(<目标名> PUBLIC|PRIVATE|INTERFACE <库名1> [库名2 ...])
# # 示例: 链接本项目定义的 my_lib (需先用 add_library 定义)
# # if(TARGET my_lib)
# #   target_link_libraries(my_app PRIVATE my_lib)
# # endif()
# # 示例: 链接外部库 (例如 POSIX Threads 和 数学库 m)
# # find_package(Threads REQUIRED) # 查找 Threads 包
# # target_link_libraries(my_app PRIVATE Threads::Threads m)

# 6. (可选) 设置编译选项或特性
# # 要求 C++17 标准
# set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED True)
# # 或者使用 target_compile_features (更现代的方式)
# # target_compile_features(my_app PUBLIC cxx_std_17)
#
# # 添加通用编译警告
# set(CMAKE_CXX_FLAGS "<span class="math-inline">\{CMAKE\_CXX\_FLAGS\} \-Wall \-Wextra \-pedantic"\)
\# \# 或者针对特定目标添加
\# \# target\_compile\_options\(my\_app PRIVATE \-Wall \-Wextra\)
\# \(可选\) 安装规则
\# install\(TARGETS my\_app DESTINATION bin\) \# 安装可执行文件到 <prefix\>/bin 目录
\# install\(FILES "</span>{CMAKE_CURRENT_SOURCE_DIR}/include/utils.h" DESTINATION include) # 安装头文件到 <prefix>/include 目录
# # 如果定义了库 my_lib, 也为其添加安装规则
# # if(TARGET my_lib)
# #   install(TARGETS my_lib
# #     ARCHIVE DESTINATION lib  # for static libraries
# #     LIBRARY DESTINATION lib  # for shared libraries on UNIX-like systems
# #     RUNTIME DESTINATION bin  # for shared libraries on Windows (DLLs)
# #   )
# # endif()
```

#### 运行 CMake (推荐核外构建 Out-of-Source Build)

核外构建可以保持源代码目录的整洁。

1. **创建构建目录并进入**：
   在项目根目录（包含 `CMakeLists.txt` 的目录）下执行：

   ```bash
   mkdir build
   cd build
   ```
2. **运行 CMake 配置和生成**：
   在 `build` 目录中执行：

   ```bash
   cmake ..
   ```

   * `..` 指向上一级目录，即 `CMakeLists.txt` 所在的目录。
   * CMake 会在此 `build` 目录中生成构建系统文件（例如 Makefiles）。
   * **常用 CMake 配置选项**：
     * `-DCMAKE_BUILD_TYPE=Debug` 或 `-DCMAKE_BUILD_TYPE=Release`：指定构建类型。Debug 版本通常包含调试信息，不做过多优化；Release 版本通常进行优化。
     * `-G "<生成器名称>"`：指定生成器。例如，在 Windows 上如果你想生成 Visual Studio 2019 的项目文件，可以使用 `-G "Visual Studio 16 2019"`。在 Linux 上，默认通常是 "Unix Makefiles"。其他常用生成器有 "Ninja"。
     * 示例：`cmake -DCMAKE_BUILD_TYPE=Release -G "Unix Makefiles" ..`
3. **执行构建**：
   CMake 配置完成后，在 `build` 目录中执行实际的构建命令：

   * 如果生成的是 Makefiles（Unix/Linux/macOS 默认）：

     ```bash
     make
     ```

     或者并行构建以加快速度（例如使用4个核心）：
     ```bash
     make -j4
     ```
   * 或者使用 CMake 的通用构建命令（推荐，因为它与所选生成器无关）：

     ```bash
     cmake --build .
     ```

     也可以指定构建配置（对于多配置生成器如 Visual Studio）：
     ```bash
     cmake --build . --config Release
     ```

     并行构建：
     ```bash
     cmake --build . --parallel 4
     ```

#### 清理构建文件

* 如果使用的是 Makefiles，并且 `Makefile` 中定义了 `clean` 目标（CMake 通常会自动生成），可以在 `build` 目录中运行：
  ```bash
  make clean
  ```
* 最简单和彻底的方法是直接删除整个 `build` 目录，然后重新创建并运行 `cmake ..`：
  ```bash
  cd .. # 回到项目根目录
  rm -rf build
  ```

---

## 4. 学习总结

通过本次对 `make` 和 `cmake` 的学习，我对这两个在软件开发中至关重要的构建工具有了更深入的理解。

`make` 是一个历史悠久且强大的工具，它通过 `Makefile` 文件中定义的规则和依赖关系来自动化编译过程。其核心优势在于能够进行增量编译，只重新构建已更改的部分，从而节省了大量的编译时间。对于结构相对简单、平台单一的项目，或者需要精细控制构建步骤的场景，`make` 仍然是一个非常有效的选择。

然而，随着项目规模的扩大和跨平台需求的增加，直接手写和维护 `Makefile` 会变得非常复杂和繁琐。这时，`CMake` 的优势就显现出来了。`CMake` 作为一个构建系统生成器，允许开发者通过更高级、更易于管理的 `CMakeLists.txt` 文件来描述项目的构建逻辑。它能够根据当前的操作系统和编译器环境，自动生成相应平台的本地构建文件（如 Makefiles、Visual Studio 项目等）。这极大地增强了项目的可移植性，并简化了复杂项目的依赖管理和配置。`CMake` 的核外构建特性也使得源代码目录能保持整洁。

我理解到，`CMake` 并非要取代 `make`（或其他本地构建工具如 Ninja），而是与它们协同工作。`CMake` 负责处理构建过程中的“配置”和“生成”阶段，而 `make` 等工具则负责实际的“构建”（编译和链接）阶段。

在未来的实践中，对于小型或特定平台的简单项目，我可能会继续使用 `make`。但对于任何有跨平台需求、或者结构较为复杂的 C/C++ 项目，我会优先考虑使用 `CMake` 来管理构建过程。我会进一步熟悉 `CMakeLists.txt` 的常用命令和模块，学习如何更好地组织项目结构、查找和链接第三方库，以及如何利用 `CMake` 的测试和打包功能，从而全面提升项目构建的自动化水平和开发效率。
