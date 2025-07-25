class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            self.coords = [0, 0]
        else:
            self.coords = coords

    def go_forward(self, arg: int = 1) -> None:
        self.coords[1] += arg

    def go_back(self, arg: int = 1) -> None:
        self.coords[1] -= arg

    def go_right(self, arg: int = 1) -> None:
        self.coords[0] += arg

    def go_left(self, arg: int = 1) -> None:
        self.coords[0] -= arg

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords: list = None) -> None:
        super().__init__(name, weight)
        if coords is None:
            self.coords = [0, 0, 0]
        else:
            self.coords = coords

    def go_up(self, arg: int = 1) -> None:
        self.coords[2] += arg

    def go_down(self, arg: int = 1) -> None:
        self.coords[2] -= arg


class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str,
                 weight: int,
                 coords: list = None,
                 max_load_weight: int = 0,
                 current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
