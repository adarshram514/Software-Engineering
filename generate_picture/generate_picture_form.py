from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField
from wtforms.validators import InputRequired

class PictureGenerationForm(FlaskForm):
    gender_option = RadioField('Choose an option', choices=[
        ('Female', 'Female'),
        ('Male', 'Male')
    ], validators=[InputRequired()])
    role_option = RadioField('Choose an option', choices=[
        ('conducting an orchestra of financial instruments like stocks, bonds, and real estate, showcasing their skill in orchestrating their investment portfolio.', 'Money Maestro'),
        ('student in a ninja outfit, wielding financial tools like calculators and charts as weapons, symbolizing their agility and precision in navigating the investment landscape.', 'Investment Ninja'),
        ('in an explorers outfit, holding a compass pointing towards financial success, having a treasure map depicting various investment opportunities', 'Market Explorer'),
        ('wearing a wizard hat with financial symbols like dollar signs and graphs in the background, symbolizing their mastery of investment knowledge.', 'Financial Wizard'),
        ('sitting on a pile of coins or surrounded by money bags, wearing a business suit and a confident smile, portraying their ambition to achieve financial success through investments.', 'Future Millionaire'),
        ('in a superhero costume with a cape made of financial newspapers or stock charts, symbolizing their ability to make smart investment decisions and conquer financial challenges', 'Investment Superhero'),
        ('with a magnifying glass examining investment opportunities, surrounded by clues like stock certificates and market reports, showcasing their detective-like approach to researching investments.', 'Investment Detective'),
        ('wearing a business casual outfit, sitting at a library table with books about stock market, finance, and economics, deep in thought over an open book, with a digital tablet displaying stock charts beside them.', 'Young Investor in a Library'),
        ('in a home office setting, with a laptop open to a "start-up" business plan, enthusiastic and ready to dive into the world of entrepreneurial finance', 'Young Entrepreneur'),
        ('analyzing cryptocurrency trends on multiple digital screens, with a background of digital currency symbols, emphasizing a focus on the modern and digital facets of investing.', 'Innovative Crypto Curator')
    ], validators=[InputRequired()])
    submit = SubmitField('Generate Picture')
