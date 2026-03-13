import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./csv/dailyActivity_merged.csv')
df.drop_duplicates(inplace=True)  

df["ActivityDate"] = pd.to_datetime(df["ActivityDate"], format="%m/%d/%Y")
df["DayOfWeek"] = df["ActivityDate"].dt.day_name()
df = df[(df["TotalSteps"] > 0) & (df["SedentaryMinutes"] < 24*60)]

steps_by_day = df.groupby("DayOfWeek")["TotalSteps"].mean().reset_index()

# sns.barplot(df,
#             x="DayOfWeek", 
#             y="TotalSteps", 
#             order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
#             errorbar=None, 
#             gap=0.2)
# plt.title("Average Total Steps by Day of the Week")
# plt.xlabel("Day of the Week")
# plt.ylabel("Average Total Steps")
# plt.show()
#Trzeba jakoś zachęcić do aktywności we wtorki i niedziele, bo w te dni ludzie są najmniej aktywni.

df2 = [
    df["VeryActiveMinutes"].mean(),
    df["FairlyActiveMinutes"].mean(),
    df["LightlyActiveMinutes"].mean(),
    df["SedentaryMinutes"].mean()
]


# plt.pie(df2, 
#         labels=["Very Active", "Fairly Active", "Lightly Active", "Sedentary"],
#          explode=(0.1, 0.1, 0.1, 0),
#          autopct='%1.1f%%',)
# plt.show()

#Widać, że większość czasu spędzamy na siedząco, więc warto zachęcić do zwiększenia aktywności fizycznej, np. poprzez krótkie przerwy na rozciąganie lub spacery w ciągu dnia.

sleep_df = pd.read_csv('./csv/minuteSleep_merged.csv')
sleep_df.drop_duplicates(inplace=True)

sleep_df["data"] = pd.to_datetime(sleep_df["date"])
sleep_df["ActivityDate"] = sleep_df["data"].dt.normalize()

real_sleep = sleep_df[sleep_df["value"] == 1]


sleep_summary = real_sleep.groupby(["Id", "ActivityDate"])["value"].sum().reset_index()
sleep_summary.rename(columns={"value": "SleepMinutes"}, inplace=True)

time_in_bed = sleep_df.groupby(["Id", "ActivityDate"])["value"].count().reset_index()

sleep_summary = sleep_summary.merge(time_in_bed, on=["Id", "ActivityDate"], how="left")
sleep_summary.rename(columns={"value": "TimeInBedMinutes"}, inplace=True)   
sleep_summary["AwakeInBedMinutes"] = sleep_summary["TimeInBedMinutes"] - sleep_summary["SleepMinutes"]

# print(sleep_summary["AwakeInBedMinutes"].mean())

# sns.histplot(sleep_summary["AwakeInBedMinutes"])
# plt.show()

#Widać, że większość osób spędza około 30 minut na byciu obudzonym w łóżku, co może wskazywać na problemy z zasypianiem lub utrzymaniem snu. Warto zachęcić do poprawy higieny snu, np. poprzez unikanie ekranów przed snem, regularne godziny snu i relaksujące rutyny przed snem.

intensity_df = pd.read_csv('./csv/hourlyintensities_merged.csv')
intensity_df["ActivityHour"] = pd.to_datetime(intensity_df["ActivityHour"])
intensity_df["Date"] = intensity_df["ActivityHour"].dt.normalize()
intensity_df["Hour"] = intensity_df["ActivityHour"].dt.hour

hour_intensity = intensity_df.groupby("Hour")["AverageIntensity"].mean().reset_index()


# sns.barplot(hour_intensity, x="Hour", y="AverageIntensity")
# plt.show()
#Godziny w których najczęściej ludzie trenują, można wysłać powiadomienie

# sns.scatterplot(df, x="TotalSteps" , y="Calories")
# sns.regplot(df, x="TotalSteps", y="Calories", scatter = False)
# plt.show()
#KROKI TO NIE WSZYSTKO!!!

sleep_summary["SleepOver8"] = sleep_summary["SleepMinutes"] > 8 * 60
sleepTime = sleep_summary.groupby("SleepOver8")["SleepOver8"].count()
# plt.pie(sleepTime,
#         labels=["No", "Yes"],
#         autopct='%1.1f%%'
#         )
# plt.title("Did sleep over 8 hours?")
# plt.show()
#71% użytkowników nie śpi przynajmniej 8 godzin

df["MadeTenTousendSteps"] = df["TotalSteps"]>8000
steps = df.groupby("MadeTenTousendSteps")["TotalSteps"].count()

# plt.pie(steps,
#         labels=["No", "Yes"],
#         autopct='%1.1f%%'
#         )
# plt.title("Did sleep over 8 hours?")
# plt.show()
#Użytkownicy nie robią 8k kroków



minuteMets = pd.read_csv("./csv/minuteMETsNarrow_merged.csv")

# minuteMets["ActivityMinute"] = minuteMets.pd.to_datetime(df["ActivityMinute"])
minuteMets["METs"] = minuteMets["METs"] / 10.0
minuteMets["Intensity"] = pd.cut(minuteMets["METs"], bins=[1.5, 3.0, 6.0, 20], labels=["lightly active", "fairly active", "very active"])
intensity = minuteMets["Intensity"].value_counts().reset_index()
print(intensity.columns)

# sns.barplot(intensity,
#              x="count",
#              y="Intensity")
# plt.show()

df["TotalWearMinutes"] = df["FairlyActiveMinutes"] + df["VeryActiveMinutes"] + df["LightlyActiveMinutes"] + df["SedentaryMinutes"]
df["WearsAllDay"] = df["TotalWearMinutes"] == 24*60
wearsAllDay = df.groupby("WearsAllDay")["WearsAllDay"].count()

# plt.pie(
#     wearsAllDay,
#     labels = ["No", "Yes"],
#     autopct='%1.1f%%'
# )

# plt.title("Did wear All day?")
# plt.show()

MeanWearTime = df["TotalWearMinutes"].mean()
# print(f"Average wear time: {MeanWearTime:1.0f} minutes, what is {MeanWearTime / 60 :1.0f} hours and {MeanWearTime % 60 :1.0f} minutes")
#Nikt nie nosi przez cały dzień


weight_df = pd.read_csv("./csv/weightLogInfo_merged.csv")

# print(df["Id"].nunique())
# print(weight_df["Id"].nunique())
#Tylko 11 z 34 uczestników zapisywało wagę, smart waga która zapisuje w apce