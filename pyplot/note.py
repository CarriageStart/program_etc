
Matplotlib.pyplot as plt
seaborn as sns



* Paper Concept
    figure  : a Piece(page) of paper
        => Denoted with Figure Id.
        => Each figure has its own pop-up window.
    subplot : a Section of page
        => Denoted as "ax" like "ax1, ax2, ax3, ax4, ..."
        => Also denoted with coordinates like (0,0), (0,1), (1,0), ...
    Canvas  : the section where the plot is drawn

1. Several Pages
    - plt focuses on the one figure.
    ex)
        fig1 = plt.figure(1, figsize=(4,3))     # Make Figure 1. If doesn't exist, create one  1 == Figure Id
        # Manipulate fig1 with plt
        plt.plot(x, y, label="plot1")
        plt.title("fig1")                       # Figure 1 title

        fig2 = plt.figure(2, figsize=(4,3))     # 2 == Figure Id
        # Manipulate fig2 with plt
        plt.plot(x, y, label="plot2")
        plt.title("fig2")                       # Figure 2 title
        plt.xlabel("x")                       # Figure 2 title
        plt.xlabel("x")                       # Figure 2 title

        plt.legend()

        plt.show()                              # Draw all figures


2. Several Section in one page
    - Auto-position consideration : 
        fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)    

    ex)
        fig, (ax1, ax2) = plt.subplots(1, 2)    # Divide the sections in the creation of a figure

        ax1.plot(x, y, label="plot1")
        ax1.set_title("subplot1")               # Set subplot title
        ax1.set_xlabel("x_subplot1")            # Set subplot labels
        ax1.set_ylabel("y_subplot1")            # Set subplot labels

        ax2.plot(x, y, label="plot2")
        ax2.set_title("subplot2")

        plt.legend()
        plt.show()                              # Draw all figure


    ex)
        fig, (ax1, ax2) = plt.subplots(1, 2)    # Divide the sections in the creation of a figure
        sns.lineplot(x=year, y=python, label="plot1", ax=ax1)
        sns.lineplot(x=year, y=python, label="plot2", ax=ax2)
        plt.show()



* Graphs
    1. line graph
        ax1.plot(x, y, label="plot1")
        plt.lineplot(year, python)
        (plt.plot(x,y, label=";;;", marker=";;;", linestyle=";;;", color=";;;"))
        sns.lineplot(x=year, y=python)

    2. label 
        plt.plot(x, y, label="plot1")
        plt.xlabel("how1")
        plt.legend()

        lp = sns.lineplot(x=year, y=python, label="plot2")
        lp.set_xlabel("how2")

    3. ticks of graph
        - In plt
        plt.xticks([1,2,3,4,...])       # Used the tick value as tick label
        plt.xticks([1,2,3,4,...], labels=["어린이", "어른", "청소년"])  # Used the label as tick label

        - In sns, it is the same.
        plt.xticks([1,2,3,4,...])


    3-1. restrict x and y
        - In both of plt and sns,
            plt.xlim(0, 7000)
            plt.ylim(0, 7000)

    4. Style
        plt.grid(True)

        sns.set_style("darkgrid")

    5. From Pandas
        - In matplot, we need to group it.
        gb_mon = df.groupby("월")
        df_mon = gb_mob.mean(numeric_only=True)
        plt.plot(df_mon["어른"], label="어른")      # Automatically use index as x data

        - in seaborn, dataframe can be used.
        sns.lineplot(data=df, x="월", y="어른", errorbar=None)  # Error bar uses 95% confidence lev.
        
    6. Bar plot
        - In plt,
        plt.bar(x, y)   # Vertical bar
        plt.barh(x, y)  # Horizontal bar

        - In sns,
        sns.barplot(df, x="요일", y="청소년", errorbar=None)
        sns.barplot(df, x="요일", y="청소년", errorbar=None, hue="공휴일")  # hue : group the data with "공휴일" col


    7. Pie chart
        - In plt,
        plt.pie(x=ratio_or_data, labels=label_data, autopct="%1.1f%%")      # autopct : value format

        - In sns,
        no pie plot exist.

    8. Histogram
        - In plt,
        plt.hist(df["어린이"], bins=10)

        - In sns,
        sns.histplot(data=df, x="어린이", binrange=(0,1000), bins=10)
        sns.histplot(data=df, x="어린이", hue="월")                         # Plotted in the same canvas
            => Overlapping can be removed with multiple="dodge" option.

    9. Box plot
        => Q2(Medain) + Q1, Q3(Box) + Whisker(bar) + points(Abnomal points)
            * IQR       : The length of box (the same unit of data) => InterQuartile Range
            * Whisker   : data region in the outside of box ,
                where 
                    maximum = min (lowest_data, Q3 + 1.5*IQR)
                    minimum = max (lowest_data, Q1 - 1.5*IQR)

                    => Data outside of whisker is represented with points

        - In plt,
            plt.boxplot(df["어린이"], df["어른"], df["청소년"])

        - In sns,
            sns.boxplot(data=df, x="월", y="어린이")    # Group by x (월)

    10. Scattered Plot
        - In plt,
            plt.scatter(df["어른"], df["청소년"])

        - In sns,
            sns.scatterplot(data=df, x="어른", y="어린이")
        

        * Correlation btw x and y
            - Calculate the correlation between columns
            df_corr = df.corr(numeric_only=True)    # Pearson Correlation
                

    11. Hit map
        - In plt,
            None
        - In sns,
            df_corr = df.corr(numeric_only=True)
            sns.heatmap(df_corr)



