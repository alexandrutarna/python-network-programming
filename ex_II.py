import csv
import os.path
import pickle
import plotly.graph_objects as go

def save_to_csv(my_dict):
    header = ('Anul', 'Cifra_afaceri')
    with open('cifra_afaceri.csv', 'w') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerow( header )

        for row in my_dict:
            file_writer.writerow((row, my_dict[row]))


def serialize_dict(my_dict):
    pickle_out = open("serialized_dict.pickle","wb")
    pickle.dump(my_dict, pickle_out)
    pickle_out.close()


def display_chart(cifra_afaceri):
    lx = []
    ly = []

    for item in cifra_afaceri:
        lx.append(item)
        ly.append(cifra_afaceri[item])

    fig = go.Figure([go.Line(x=lx, y=ly)])
    fig.update_layout(title='Cifra de afaceri in intervalul 2010-2017',
                    xaxis_title='Anul',
                    yaxis_title='Cifra de afaceri (EURO)'
                    )
    fig.show()

if __name__ == "__main__":
    
    # a
    cifra_afaceri = {
        '2010' : 230000, 
        '2011' : 280000,
        '2012' : 310000, 
        '2013' : 320000, 
        '2014' : 350000, 
        '2015' : 310000, 
        '2016' : 380000, 
        '2017' : 400000
    }


    # b
    save_to_csv(cifra_afaceri)

    # c 
    serialize_dict(cifra_afaceri)

    # d
    display_chart(cifra_afaceri)
