import matplotlib.pyplot as plt

data_toyama = []
data_ishikawa = []
data_fukui = []

day = 1

rain = 3
rain_flag = 4

wind = 7
wind_flag = 8

templature = 9
templature_flag = 10

with open("AMEDAS_data_Hokuriku3CSV.dat", "r", encoding = "UTF-8") as file:
    
    for line in file:
      datalist = [i for i in line.split()]
      for i in range(13):
          if i != 5:
              datalist[i] = float(datalist[i])

      if datalist[0] == 55102:
          data_toyama.append(datalist)
      elif datalist[0] == 56227:
          data_ishikawa.append(datalist)
      else:
          data_fukui.append(datalist)

    datalist_len = len(datalist)
    data_toyama_len = len(data_toyama)
    data_ishikawa_len = len(data_ishikawa)
    data_fukui_len = len(data_fukui)


    def average(data, data_len, item, flag):
      sum_count = 0
      totall = 0
      for i in range(data_len):
        if  data[i][flag] <= 3:
          totall += data[i][item]
          sum_count += 1
      av = totall / sum_count
      return av
    
    def month_average(data, data_len, item, flag, date):
        av_list_month = []
        av_list_year = []
        sum_count = 0
        totall = 0
        now_month = data[0][date] // 100
        now_year = data[0][date] // 10000

        for i in range(data_len):
          if data[i][date] // 100 == now_month:
            if data[i][flag] <= 3:
              totall += data[i][item]
              sum_count += 1
              av = totall/sum_count
              
          else:
            av_list_month.append(av)
            sum_count = 0
            totall = 0
            now_month = data[i][date] // 100
            if data[i][flag] <= 3:
               totall += data[i][item]
               sum_count += 1
          if data[i][date] // 10000 != now_year:
             av_list_year.append(av_list_month)
             now_year = data[i][date] // 10000
             av_list_month = []

        return av_list_year

    toyama_rain_av = average(data_toyama, data_toyama_len, rain, rain_flag)
    print("富山の2008/11/18-2008/12/31までの平均の降水量は" + str(toyama_rain_av) + "mm")

    toyama_wind_av = average(data_toyama, data_toyama_len, wind, wind_flag)
    print("　　　　　　　　　　　　　　　　　　　　風速は" + str(toyama_wind_av) + "m/s")

    toyama_templature_av = average(data_toyama, data_toyama_len, templature, templature_flag)
    print("　　　　　　　　　　　　　　　　　　　　気温は" + str(toyama_templature_av) + "℃")


    ishikawa_rain_av = average(data_ishikawa, data_ishikawa_len, rain, rain_flag)
    print("石川の2008/11/18-2008/12/31までの平均の降水量は" + str(ishikawa_rain_av) + "mm")

    ishikawa_wind_av = average(data_ishikawa, data_ishikawa_len, wind, wind_flag)
    print("　　　　　　　　　　　　　　　　　　　　風速は" + str(ishikawa_wind_av) + "m/s")

    ishikawa_templature_av = average(data_ishikawa, data_ishikawa_len, templature, templature_flag)
    print("　　　　　　　　　　　　　　　　　　　　気温は" + str(ishikawa_templature_av) + "℃")


    fukui_rain_av = average(data_fukui, data_fukui_len, rain, rain_flag)
    print("福井の2008/11/18-2008/12/31までの平均の降水量は" + str(fukui_rain_av) + "mm")

    fukui_wind_av = average(data_fukui, data_fukui_len, wind, wind_flag)
    print("　　　　　　　　　　　　　　　　　　　　風速は" + str(fukui_wind_av) + "m/s")

    fukui_templature_av = average(data_fukui, data_fukui_len, templature, templature_flag)
    print("　　　　　　　　　　　　　　　　　　　　気温は" + str(fukui_templature_av) + "℃")

    average_list_toyama = month_average(data_toyama, data_toyama_len, templature, templature_flag, day)

    average_list_ishikawa = month_average(data_ishikawa, data_ishikawa_len, templature, templature_flag, day)

    average_list_fukui = month_average(data_fukui, data_fukui_len, templature, templature_flag, day)

    
    def graph(data, location):
      Y = []
      plt.xlabel("month")
      plt.ylabel("templature[℃]")
      print(len(data))
      for i in range(len(data)):
        plt.title(location + ":" + str(2008 + i) )
        X = [j for j in range(1, len(data[i]) + 1)]
        if i == 0:
           X = [11, 12]
        Y.append(data[i])
        plt.plot(X, Y[i], marker = ".")
        a = 2
        for j in range(len(data[i])):
           plt.text(X[j], Y[i][j] -1, str(round(Y[i][j], 2)))
        plt.show()

    graph(average_list_toyama, "Toyama")
    graph(average_list_ishikawa, "Ishikawa")
    graph(average_list_fukui, "Fukui")






