# Erbert & Gerbert's Checker
A simple brute-force balance checker for the sandwich chain Erbert &amp; Gerbert's.

This tool was created in early August 2020. It might seem a little off as I was not as familiar with the Python langauge back then as I am today. All this tool does is visit Erbert & Gerbert's website and input in an incrementing number. Afterwards, it grabs the balance, and if it is higher than $0.00, it writes it to a file. 

### What could be done to prevent this?

1. Adding a limit of checks per IP would be the first step. In the current state, one user could check any amount of cards as they want. This security measure could be bypassed via the use of proxies. In order to make it more expensive, they could limit the countries of the IPs that can check cards.

2. Next, add reCAPTCHA. As it stands, there is no captcha measures implemented, meaning that it is very easy to check your balance. Yet again, this security measure could be thwarted via captcha solving services.

3. In terms of issuing new cards, a PIN code would help defeat attackers. If one needs proxies, a captcha solver, *and* a PIN code, it becomes even more unreasonable to spend time attacking this website. The PIN code can be beaten by brute force tools, so the larger the PIN, the better!

4. Again, for new cards, they could create an algorithm that all cards must follow. Rather than assign cards sequentially, algorithms would make it harder for one to guess the next card, especially if it was not a commonly used one such as the Luhn algorithm. Unfortunately at the moment, one could simply be a regular customer, buy a card, accidentally mistype the number, and they'd come across another card that might have balance!

There's more security measures that could be put in place, but I am simply a hobbyist and I'm unaware of *every* potential security measure, I simply listed the ones that I would use if I were creating a giftcard system. 
