def obter_info_alunos(qnt_alunos: int) -> dict[str, int]:
    # Pega duas informações separadas por espaço e guarda em um dicionário.
    alunos: dict[str, int] = {}
    for _ in range(qnt_alunos):
        info: list[str] = input().split(" ")
        nome, habilidade, *_ = info 
        alunos[nome] = int(habilidade)
    return alunos

def ordenar_por_habilidade(qnt_alunos: int, alunos: dict[str, int]) -> list[str]:
    # Ordena os alunos em ordem decrescente de habilidade.
    alunos_h: list[str] = []
    for _ in range(qnt_alunos):
        target = max(alunos, key=alunos.get)
        del alunos[target]
        alunos_h.append(target)
        
    return alunos_h

def criar_times(num_time: int) -> list[set]:
    # Crie a quantidade certa de times, baseado no parâmetro.
    times: list[set] = []
    for _ in range(num_time):
        times.append(set())
    return times

def distribuir_alunos(qnt_alunos: int, times: list[set], alunos: list[str]) -> list[list]:
    # Coloca os alunos nos times e ordena em ordem alfabetica.
    for i in range(qnt_alunos):
        times[i % len(times)].add(alunos[i])
    
    ordem_alfabetica: list[list] = []
    for i in range(len(times)):
       ordem_alfabetica.append(sorted(times[i]))

    return ordem_alfabetica

def exibir_times(times: list[list]):
    for i, v in enumerate(times):
        print(f"Time {i + 1}")
        print(*v, sep="\n")
        print()


def main():
    try:
        entrada: list[str] = input().split(" ")
        qnt_alunos, num_time, *_ = entrada

        alunos = obter_info_alunos(int(qnt_alunos))
        nivel_de_habilidade = ordenar_por_habilidade(int(qnt_alunos), alunos)
        times = criar_times(int(num_time))
        resultado = distribuir_alunos(int(qnt_alunos), times, nivel_de_habilidade)

        exibir_times(resultado)
    except ValueError:
        pass

if __name__ == "__main__":
    main()