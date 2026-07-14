from system.initialization_system.game_localization import GameLocalization

class Window:
    def __init__(self, x, y, width, height, title="", content=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.content = GameLocalization.translate(content)


    def draw(self, screen):
        x = self.x
        y = self.y
        w = self.width
        h = self.height

        screen[y][x] = "┌"
        screen[y][x+w-1] = "┐"

        for i in range(1, w-1):
            screen[y][x+i] = "─"

        screen[y+h-1][x] = "└"
        screen[y+h-1][x+w-1] = "┘"

        for i in range(1, w-1):
            screen[y+h-1][x+i] = "─"

        for i in range(1, h-1):
            screen[y+i][x] = "│"
            screen[y+i][x+w-1] = "│"

        title = f" {self.title} "

        for i, char in enumerate(title[:w]):
            screen[y][x+2+i] = char

        #---------------------------------------------
        # Determina quantas linhas podem ser exibidas
        # dado o tamanho da janela. Dois espaços são
        # ocupados pelas bordas superior e inferior.
        #---------------------------------------------
        visible_height = h - 2

        #Se houver mais conteudo do que espaço disponivel,
        #reserva uma linha para o indicador de intens ocultos.
        remaining = visible_height - 1

        # -------------------------------------------------
        # Quando o conteúdo ultrapassa a altura da janela,
        # exibe apenas os itens mais recentes juntamente
        # com um indicador de continuidade.
        # -------------------------------------------------
        hidden = len(self.content) - remaining
        visible_content = [
            f"{GameLocalization.get(
                "system.ui.message_up",
                hidden=hidden,
            )}"
        ]
        visible_content.extend(
            self.content[-remaining:]
        )

        if len(self.content) <= visible_height:
            for i, line in enumerate(self.content[:h-2]):
                for j, char in enumerate(line[:w-2]):
                    screen[y+1+i][x+1+j] = char

        else:
            for i, line in enumerate(visible_content[:h-2]):
                for j, char in enumerate(line[:w-2]):
                    screen[y+1+i][x+1+j] = char


class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.windows = []

    def add(self, window):
        self.windows.append(window)

    def render(self):
        screen = [
            [" " for _ in range(self.width)]
            for _ in range(self.height)
        ]

        for window in self.windows:
            window.draw(screen)

        for row in screen:
            print("".join(row))