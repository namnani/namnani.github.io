---
layout: post
title:  "Java 의문사항 정리"
date:   2019-01-16 05:20:59 +0900
author: Namnani
categories: Java_Question
tags: Java Question
---
---
#### 1. 왜 항상 hashCode와 equals 메소드를 같이 재정의해야하는가?
  - Hash계열에서 hashCode를 쓰고, 나머지는 equals()를 사용하는 것 같으니 필요에 따라 재정의 하면 되는 것이 아닌가?

#### 2. 설계 시에 상속이 결정난다고 하는데, interface도 설계시에 결정나야 하는가?
  - 코딩후에 interface를 뽑아낼수도 있을 것 같은데.

#### 3. this가 스택에 쌓인다고 했는데,, 흠,,
  - 내 생각에는, 힙에 있어야 할 것 같은데,, 메소드안에서 참조하기도 하니까.
