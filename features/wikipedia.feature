Feature: Validar información histórica de automatización en Wikipedia

  Scenario: Validar el primer proceso automático
    Given el usuario navega a Wikipedia
    When busca la palabra "automatización"
    Then se muestra el año del primer proceso automatico
    And se toma una captura de la pagina
