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
    return amount * value


def calculate_profit_loss_per_coin(currentValue, amountPaid):
    return currentValue - amountPaid


def calculate_profit_loss_totals(current_profit_loss, amount_of_coins):
    return current_profit_loss * amount_of_coins


def format_price(value):
    return "{:.2f}".format(value)


def paid_price_per_coin(amount_paid, amount_of_coins):
    return amount_paid / amount_of_coins


def format_currency(value, currencySymbol):
    return f"{currencySymbol}{value}"


def print_profit_loss(value):
    if(value) > 0:
        return "green"

    return "red"


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

    name = Label(gui, text="Current Total Value", bg="#142E54", fg="white",
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
    total_pl = 0
    total_current_value = 0

    for token, market in portfolio:
        symbol = Label(gui, text=market.symbol, bg="#F3F4F6", fg="black",
                       font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        symbol.grid(row=coin_row, column=0, sticky=N+S+E+W)

        lbl_current_price = Label(gui, text=format_currency(format_price(market.current_price), "$"),
                                  bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        lbl_current_price.grid(row=coin_row, column=1, sticky=N+S+E+W)

        lbl_amount_owned = Label(gui, text=token.amount_owned, bg="#F3F4F6", fg="black", font="Lato 12 bold",
                                 padx="2", pady="2", borderwidth=2, relief="groove")
        lbl_amount_owned.grid(row=coin_row, column=2, sticky=N+S+E+W)

        lbl_amount_paid = Label(gui, text=format_currency(token.amount_paid, "$"),
                                bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        lbl_amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

        current_value = calculate_value(
            token.amount_owned, market.current_price)
        lbl_current_value = Label(gui, text=format_currency(format_price(current_value), "$"), bg="#F3F4F6", fg="black", font="Lato 12 bold",
                                  padx="2", pady="2", borderwidth=2, relief="groove")
        lbl_current_value.grid(row=coin_row, column=4, sticky=N+S+E+W)

        profit_loss_per_coin = calculate_profit_loss_per_coin(
            market.current_price, paid_price_per_coin(token.amount_paid, token.amount_owned))
        lbl_profit_loss_per_coin = Label(gui, text=format_currency(format_price(profit_loss_per_coin), "$"), bg="#F3F4F6", fg=print_profit_loss(profit_loss_per_coin),
                                         font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        lbl_profit_loss_per_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

        total_profit_loss_with_coin = calculate_profit_loss_totals(calculate_profit_loss_per_coin(
            market.current_price, paid_price_per_coin(token.amount_paid, token.amount_owned)), token.amount_owned)
        lbl_total_profit_loss_with_coin = Label(gui, text=format_currency(format_price(total_profit_loss_with_coin), "$"), bg="#F3F4F6", fg=print_profit_loss(total_profit_loss_with_coin),
                                                font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        lbl_total_profit_loss_with_coin.grid(
            row=coin_row, column=6, sticky=N+S+E+W)
        coin_row = coin_row + 1
        total_pl = total_pl + total_profit_loss_with_coin
        total_current_value = total_current_value + current_value

    lbl_totals = Label(gui, text="Totals: ", bg="#F3F4F6", fg="black",
                       font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
    lbl_totals.grid(row=coin_row, column=0, columnspan=4, sticky=N+S+E+W)

    lbl_total_profits = Label(gui, text=format_currency(format_price(total_current_value), "$"), bg="#F3F4F6", fg="black",
                              font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
    lbl_total_profits.grid(row=coin_row, column=4, sticky=N+S+E+W)

    lbl_total_profits = Label(gui, text=format_currency(format_price(total_pl), "$"), bg="#F3F4F6", fg=print_profit_loss(total_pl),
                              font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
    lbl_total_profits.grid(row=coin_row, column=6, sticky=N+S+E+W)


draw_header(pycrypto)
draw_portfolio(pycrypto, viewModel)
pycrypto.mainloop()
