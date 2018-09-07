#GI(D)
Gini_index_Entire_Data_set = 1.0 - ( 5.0 / 14.0 ) ** 2 - ( 9.0 / 14.0 ) ** 2;

#GI(DSunny) 
Gini_index_Outlook_Sunny = 1 - ( 2.0 / 5.0 ) ** 2 - ( 3.0 / 5.0 ) ** 2;

#GI(DOvercast) 
Gini_index_Outlook_Overcast = 1 - ( 4.0 / 4.0 ) ** 2;

#GI(DRainy)
Gini_index_Outlook_Rainy = 1 - ( 3.0 / 5.0 ) ** 2 - ( 2.0 / 5.0 ) ** 2;

#GG(D, Outlook)
Gini_Gain_Outlook = Gini_index_Entire_Data_set - ( 5.0 / 14.0 ) * Gini_index_Outlook_Sunny - ( 4.0 / 14.0 ) * Gini_index_Outlook_Overcast - ( 5.0 / 14.0 ) * Gini_index_Outlook_Rainy;

#GI(DHot)
Gini_index_Temperature_Hot = 1 - ( 2.0 / 4.0 ) ** 2 - ( 2.0 / 4.0 ) ** 2;

#GI(DMild) 
Gini_index_Temperature_Mild = 1 - ( 4.0 / 6.0 ) ** 2 - ( 2.0 / 6.0 ) ** 2;

#GI(DCool) 
Gini_index_Temperature_Cool = 1 - ( 3.0 / 4.0 ) ** 2 - ( 1.0 / 4.0 ) ** 2;

#GG(D, Tempature)
Gini_Gain_Tempature = Gini_index_Entire_Data_set - ( 4.0 / 14.0 ) * Gini_index_Temperature_Hot - ( 6.0 / 14.0 ) * Gini_index_Temperature_Mild - ( 4.0 / 14.0 ) * Gini_index_Temperature_Cool;

#GI(DHigh)
Gini_index_Humidity_High = 1 - ( 3.0 / 7.0 ) ** 2 - ( 4.0 / 7.0 ) ** 2;

#GI(DNormal) 
Gini_index_Humidity_Normal = 1 - ( 6.0 / 7.0 ) ** 2 - ( 1.0 / 7.0 ) ** 2;

#GG(D, Humidity) 
Gini_Gain_Humidity = Gini_index_Entire_Data_set - ( 7.0 / 14.0 ) * Gini_index_Humidity_High - ( 7.0 / 14.0 ) * Gini_index_Humidity_Normal;

#GI(DTrue) 
Gini_index_Windy_True = 1 - ( 3.0 / 6.0 ) ** 2 - ( 3.0 / 6.0 ) ** 2;

#GI(DFalse) 
Gini_index_Windy_False = 1 - ( 6.0 / 8.0 ) ** 2 - ( 2.0 / 8.0 ) ** 2;

#GG(D, Windy) 
Gini_Gain_Windy =  Gini_index_Entire_Data_set - ( 6 / 14 ) * Gini_index_Windy_True - ( 8 / 14) * Gini_index_Windy_False;

#GI(DSunnyHot) 
Gini_index_Sunny_Hot = 1 - ( 2.0 / 2.0 ) ** 2;
print(Gini_index_Sunny_Hot);

#GI(DSunnyMild)
Gini_index_Sunny_Mild = 1 - ( 1.0 / 2.0 ) ** 2  - ( 1.0 / 2.0 ) ** 2;
print(Gini_index_Sunny_Mild);

#GI(DSunnyCool)
Gini_index_Sunny_Cool = 1 - ( 1.0 / 1.0 ) ** 2;
print(Gini_index_Sunny_Cool);

#GG(Sunny, Tempature) 
Gini_Gain_Sunny_Temperature = Gini_index_Outlook_Sunny - ( 2 / 5 ) * Gini_index_Sunny_Hot - ( 2.0 / 5.0 ) * Gini_index_Sunny_Mild  - ( 1.0 / 5.0 ) * Gini_index_Sunny_Cool;
print(Gini_Gain_Sunny_Temperature);

#GI(DSunnyHigh)
Gini_index_Sunny_High = 1 - ( 3.0 / 3.0 ) ** 2;
print(Gini_index_Sunny_High);