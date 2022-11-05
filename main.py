from api import coingecko_service as cgapi
from tkinter import *
from models import portfolio as p, token as t

portfolio = p.Portfolio()
portfolio.tokens.append(t.Token("Ethereum", 13, 5500))
portfolio.tokens.append(t.Token("Bitcoin", 2, 16000))
portfolio.tokens.append(t.Token("Litecoin", 10, 400))

marketData = cgapi.get_market(list(t.name for t in portfolio.tokens))
viewModel = list(
    zip(sorted(portfolio.tokens, key=lambda x: x.name, reverse=False), marketData))

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')


def draw_portfolio(portfolio):
    coin_row = 1

    for token, market in portfolio:
        name = Label(pycrypto, text=market.symbol, bg="#F3F4F6", fg="black",
                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=0, sticky=N+S+E+W)

        name = Label(pycrypto, text=market.current_price,
                     bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=1, sticky=N+S+E+W)

        name = Label(pycrypto, text=token.amount_owned, bg="#F3F4F6", fg="black", font="Lato 12 bold",
                     padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=2, sticky=N+S+E+W)

        name = Label(pycrypto, text=token.amount_paid,
                     bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=3, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black", font="Lato 12 bold",
                     padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=4, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black",
                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=5, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black",
                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=6, sticky=N+S+E+W)
        coin_row = coin_row + 1


def draw_header(pycrypto):
    name = Label(pycrypto, text="Coin Name", bg="#142E54",
                 fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=0, sticky=N+S+E+W)

    name = Label(pycrypto, text="Price", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=1, sticky=N+S+E+W)

    name = Label(pycrypto, text="Coins Owned", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=2, sticky=N+S+E+W)

    name = Label(pycrypto, text="Total Amount Paid", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=3, sticky=N+S+E+W)

    name = Label(pycrypto, text="Current Value", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=4, sticky=N+S+E+W)

    name = Label(pycrypto, text="P/L per Coin", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=5, sticky=N+S+E+W)

    name = Label(pycrypto, text="Total P/L With coin", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=6, sticky=N+S+E+W)


draw_header(pycrypto)
draw_portfolio(viewModel)
pycrypto.mainloop()
