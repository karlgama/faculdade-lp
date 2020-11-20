#Kaique Silva Grangeiro RA: 1903564
#Felipe Freire Lopes RA: 1903226
#Ricardo Antonio Gonçalves da Silva RA: 1903013
#Breno Francisco de Oliveira RA:1904367
from clinic import Paciente
from clinic import Medico
from clinic import Quarto


def main():
    medico = Medico("1111111111", "55856325156", "54848559625704", "Ricardo",
                    "1141423419", "8000", "Ortopedista")

    paciente = Paciente("João", "46598241", "25687445801",
                        "Rua Ametista, 502, Jardim Paulist, São Paulo-SP",
                        "11953151460", "30-08-1994", medico)

    quarto = Quarto("504", "2")
    internacao = quarto.internar(paciente)

    estado = paciente.atualizarEstado("Paciente se encontra estável", "17:50",
                                      medico.nome)
    print(estado)
    print(internacao)
    print(medico.exibirMedico())
    print(quarto.exibirQuarto())
    print(paciente.exibirPaciente())
    print(paciente.getQuarto())

main()
