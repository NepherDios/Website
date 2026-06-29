#!/usr/bin/env python3

from pathlib import Path
import shutil

BASE = Path.cwd()

# source file -> destination folder
PRODUCTS = {
    "caboclos":              "canecas/religiao/umbanda/000001-caboclo",
    "orixa_ogum":            "canecas/religiao/umbanda/000002-ogum",
    "orixa_oxala":           "canecas/religiao/umbanda/000003-oxala",
    "pretos_velhos":         "canecas/religiao/umbanda/000004-pretos_velhos",
    "ze_pelintra":           "canecas/religiao/umbanda/000005-ze_pelintra",
    "caneca_de_oxumare":     "canecas/religiao/umbanda/000006-oxumare",

    "nossa_sr_fatima":       "canecas/religiao/catolicismo/000001-fatima",
    "santo_antonio":         "canecas/religiao/catolicismo/000002-santo_antonio",
    "sao_joao":              "canecas/religiao/catolicismo/000003-sao_joao",
    "sao_pedro":             "canecas/religiao/catolicismo/000004-sao_pedro",
    "senhor_dos_passos":     "canecas/religiao/catolicismo/000005-senhor_dos_passos",

    "clube_flamengo":        "canecas/desporto/futebol/000001-clube_flamengo",
    "clube_porto":           "canecas/desporto/futebol/000002-clube_porto",
    "portugal_selecao":      "canecas/desporto/futebol/000003-portugal_selecao",

    "signo_peixes":          "canecas/signos/000001-peixes",
    "signo_gemeos":          "canecas/signos/000002-gemeos",
    "signo_balanca":         "canecas/signos/000003-balanca",

    "ferrari":               "canecas/carros/000001-ferrari",

    "caneca_red_dead_redemption":
                              "canecas/jogos/000001-red_dead_redemption",

    "keep_calm_self_believe":
                              "canecas/frases/000001-keep_calm_self_believe",
}


def move_product(name, folder):

    folder = BASE / folder
    folder.mkdir(parents=True, exist_ok=True)

    webp = BASE / f"{name}.webp"
    jpeg = BASE / f"{name}.jpeg"

    if webp.exists():
        dst = folder / "main.webp"

        if dst.exists():
            print(f"SKIP {dst}")
        else:
            shutil.move(str(webp), str(dst))
            print(f"Moved {webp.name}")

    if jpeg.exists():
        dst = folder / "backup_main.jpeg"

        if dst.exists():
            print(f"SKIP {dst}")
        else:
            shutil.move(str(jpeg), str(dst))
            print(f"Moved {jpeg.name}")


def main():

    for product, folder in PRODUCTS.items():
        move_product(product, folder)

    print("\nFinished.")


if __name__ == "__main__":
    main()
