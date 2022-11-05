from api import coingecko_service as cgapi
from tkinter import *
from models import portfolio as p, token as t

portfolio = p.Portfolio()
portfolio.tokens.append(t.Token("Ethereum", 13, 5500))
portfolio.tokens.append(t.Token("Bitcoin", 2, 16000))
portfolio.tokens.append(t.Token("Litecoin", 10, 400))

marketData = cgapi.get_market(list(t.name for t in portfolio.tokens))
viewModel = list(
    zip(portfolio.get_tokens_sorted(), marketData))

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')


def calculate_value(amount, value):
    return format_price(amount * value)


def format_price(value):
    return "{:.2f}".format(value)


def format_currency(value, currencySymbol):
    return f"{value}{currencySymbol}"


def draw_header(gui):
    name = Label(gui, text="Coin Name", bg="#142E54",
                 fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=0, sticky=N+S+E+W)

    name = Label(gui, text="Price", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=1, sticky=N+S+E+W)

    name = Label(gui, text="Coins Owned", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=2, sticky=N+S+E+W)

    name = Label(gui, text="Total Amount Paid", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=3, sticky=N+S+E+W)

    name = Label(gui, text="Current Value", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=4, sticky=N+S+E+W)

    name = Label(gui, text="P/L per Coin", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=5, sticky=N+S+E+W)

    name = Label(gui, text="Total P/L with coin", bg="#142E54", fg="white",
                 font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=6, sticky=N+S+E+W)


def draw_portfolio(gui, portfolio):
    coin_row = 1

    for token, market in portfolio:
        symbol = Label(gui, text=market.symbol, bg="#F3F4F6", fg="black",
                       font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        symbol.grid(row=coin_row, column=0, sticky=N+S+E+W)

        current_price = Label(gui, text=format_price(market.current_price),
                              bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        current_price.grid(row=coin_row, column=1, sticky=N+S+E+W)

        amount_owned = Label(gui, text=token.amount_owned, bg="#F3F4F6", fg="black", font="Lato 12 bold",
                             padx="2", pady="2", borderwidth=2, relief="groove")
        amount_owned.grid(row=coin_row, column=2, sticky=N+S+E+W)

        amount_paid = Label(gui, text=format_currency(token.amount_paid, "€"),
                            bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

        current_value = Label(gui, text=calculate_value(token.amount_owned, market.current_price), bg="#F3F4F6", fg="black", font="Lato 12 bold",
                              padx="2", pady="2", borderwidth=2, relief="groove")
        current_value.grid(row=coin_row, column=4, sticky=N+S+E+W)

        profit_loss_per_coin = Label(gui, text="0", bg="#F3F4F6", fg="black",
                                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        profit_loss_per_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

        total_profit_loss_with_coin = Label(gui, text="0", bg="#F3F4F6", fg="black",
                                            font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        total_profit_loss_with_coin.grid(
            row=coin_row, column=6, sticky=N+S+E+W)
        coin_row = coin_row + 1


draw_header(pycrypto)
draw_portfolio(pycrypto, viewModel)
pycrypto.mainloop()
