# 단일 책임 원칙(Single Responsibility Priciple, SRP)
 * 책임 = 변경이유
 * 단일 책임 = 관심사 분리
 - 여러 책임을 가졌을 시에는, 수정이 일어나면 다른 모듈에 어떠한 영향을 미치는지 범위를 추측하기 힘듦.
 
 # 개방 / 폐쇄 원칙 (Open / Closed Principle, OCP)
  * 모듈 함수등의 소프트웨어 개체는 확장에 대해 열려있어야 하고, 수정에 대해서는 닫혀 있어야 한다는 원칙.
  * 수정이 일어나더라도 기존의 구성요소에는 수정이 일어나지 않아야 하며, 쉽게 확장이 가능하여 재사용을 할 수 있도록 해야한다는 뜻.
  * 추상화와 다형성
  * 다형성 - 여러 가지 형태를 가질 수 있는 능력 <- 유연성, 재사용성, 유지보수성 등을 위해
