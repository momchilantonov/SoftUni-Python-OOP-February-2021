from typing import List

from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors: List[Survivor] = []
        self.supplies: List[Supply] = []
        self.medicine: List[Medicine] = []

    @property
    def food(self):
        food: List[FoodSupply] = [f for f in self.supplies if isinstance(f, FoodSupply)]
        if not food:
            raise IndexError("There are no food supplies left!")
        return food

    @property
    def water(self):
        water: List[WaterSupply] = [w for w in self.supplies if isinstance(w, WaterSupply)]
        if not water:
            raise IndexError("There are no water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers: List[Painkiller] = [pk for pk in self.medicine if isinstance(pk, Painkiller)]
        if not painkillers:
            raise IndexError("There are no painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves: List[Salve] = [s for s in self.medicine if isinstance(s, Salve)]
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        medicine = None
        for idx in range(len(self.medicine)-1, -1, -1):
            if self.medicine[idx].__class__.__name__ == medicine_type:
                medicine = self.medicine.pop(idx)
                break
        if survivor.needs_healing and medicine:
            medicine.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        sustenance = None
        for idx in range(len(self.supplies)-1, -1, -1):
            if self.supplies[idx].__class__.__name__ == sustenance_type:
                sustenance = self.supplies.pop(idx)
                break
        if survivor.needs_sustenance and sustenance:
            sustenance.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
