library(ggplot2)
library(reshape2)
setwd('/Users/stephaniewankowicz/Dropbox/BMI_203/190109_git_travis_example/')
bubble<-read.csv('complexity_df_bubblesort.csv')
quick<-read.csv('complexity_df_quicksort.csv')

quick_m<-melt(quick)
quick_m_assign<-quick_m[grep('assign',quick_m$variable), ]
quick_m_cond<-quick_m[grep('cond',quick_m$variable), ]

ggplot(data=quick_m_assign, aes(x=variable,value, colour=value)) +geom_point()+theme_bw()+scale_fill_brewer(palette = 'red')+theme(axis.text.x = element_text(angle = 60, hjust = 1), legend.position="bottom")+labs(x='Number of Items to Sort', y='Number of Assignments', title = 'Quicksort')
ggplot(data=quick_m_cond, aes(x=variable,value)) +geom_point()+ theme_bw()+scale_fill_brewer(palette = 'Reds')+theme(axis.text.x = element_text(angle = 60, hjust = 1), legend.position="bottom")+labs(x='Number of Items to Sort', y='Number of Conditionals', title = 'Quicksort')

bubble_m<-melt(bubble)
#bubble_m$variable<-gsub('X','', bubble_m$variable)
bubble_m_assign<-bubble_m[grep('assign',bubble_m$variable), ]
bubble_m_cond<-bubble_m[grep('cond',bubble_m$variable), ]
ggplot(data=bubble_m_assign, aes(x=variable,value)) +geom_point(aes(colour = value))+theme_bw()+scale_fill_brewer(palette = "Greens")+theme(axis.text.x = element_text(angle = 60, hjust = 1), legend.position="bottom")+labs(x='Number of Items to Sort', y='Number of Assignments', title = 'Bubblesort')
ggplot(data=bubble_m_cond, aes(x=variable,value)) +geom_point(aes(colour = value))+ theme_bw()+scale_fill_brewer(palette = 'Reds')+theme(axis.text.x = element_text(angle = 60, hjust = 1), legend.position="bottom")+labs(x='Number of Items to Sort', y='Number of Conditionals', title = 'Bubblesort')

