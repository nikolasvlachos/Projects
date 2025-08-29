#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//*****************************************************************************************************************************
//*****************************************************************************************************************************
// DEFINE START AND END YEARS FOR QUESTIONS INVOLVING YEARLY AVERAGES
// DEFINE MONTHS

#define START_YEAR 1760
#define END_YEAR 2015

#define START_YEAR2 1850
#define END_YEAR2 2015

const char *months[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
                        
int main(void){
	
//*****************************************************************************************************************************
//*****************************************************************************************************************************
// INITIALIZE ARRAYS AND VARIABLES FOR ALL QUESTIONS
	
	// Variables and arrays for data extraction
	char buffer[1000];
    char year_str[5], month_str[3];
    int year, month;
    float temperature, temp_oce, uncertainty;
    
    // Arrays for question 1 and 6
    float yearly_sum[END_YEAR - START_YEAR + 1] = {0};
    int yearly_count[END_YEAR - START_YEAR + 1] = {0};
    
    // Arrays for question 2
    float century_sum[4] = {0}; // 18th, 19th, 20th, 21st century
    int century_count[4] = {0}; // 18th, 19th, 20th, 21st century

    // Arrays for question 3    
    float monthly_sum[12] = {0}; // Sum of temperatures for each month
    int monthly_count[12] = {0}; // Number of temperature readings for each month
    
    // Variables and Arrays for question 4
	float hottest_temperature = 0;
    float coldest_temperature = 100;
    char hottest_month[20];
    char coldest_month[20];
    
    // Variables and Arrays for question 5 
    int hottest_year, coldest_year;
    float hottest_year_temp = 0;
    float coldest_year_temp = 1000;
    int hottest_year_recorded;
    int coldest_year_recorded;
    
    // Arrays for question 7
    double c_19[100];
    double c_20[100];
    
    // variables and arrays for question 8 and 9
    float temperature_max;
    float temperature_min;
    
    // q8
    float yearly_sum_q8[END_YEAR2 - START_YEAR2 + 1] = {0};
	float yearly_sum_max_q8[END_YEAR2 - START_YEAR2 + 1] = {0};
	float yearly_sum_min_q8[END_YEAR2 - START_YEAR2 + 1] = {0};
    int yearly_count_q8[END_YEAR2 - START_YEAR2 + 1] = {0};
    
    // q9
    float century_sum_max_q9[3];
    float century_sum_min_q9[3];
    float century_sum_q9[3] = {0}; // 18th, 19th, 20th, 21st century
    int century_count_q9[3] = {0}; // 19th, 20th, 21st century

    
    // Arrays for question 10
    float monthlyq10_sum[12] = {0}; 
    int monthlyq10_count[12] = {0}; 
    float q10_unc_sum[12] = {0}; 
    int q10_unc_count[12] = {0}; 
    
	// Arrays for question 11
    float yearlyq11_sum[END_YEAR2 - START_YEAR2 + 1] = {0}; 
    int yearlyq11_count[END_YEAR2 - START_YEAR2 + 1] = {0}; 
    float yearlyq11_sum_oce[END_YEAR2 - START_YEAR2 + 1] = {0}; 
    int yearlyq11_count_oce[END_YEAR2 - START_YEAR2 + 1] = {0}; 
    
    
//*****************************************************************************************************************************
//*****************************************************************************************************************************
// DATA EXTRACTION FOR ALL QUESTIONS
    
	FILE *GlobalTempsFile = fopen("GlobalTemperatures.csv", "r");
	if (GlobalTempsFile == NULL){
		printf("Error: could not open file\n");
		exit(-1);
	}
	
	while(fgets(buffer, sizeof(buffer), GlobalTempsFile)){
		sscanf(buffer, "%4s-%2s-%*2s,%f,%f,%f,%*f,%f,%*f,%f", year_str, month_str, &temperature, &uncertainty, &temperature_max, &temperature_min, &temp_oce);
        year = atoi(year_str);
        month = atoi(month_str);
        if (year >= START_YEAR && year <= END_YEAR) {
			
			// Most of the data extractions involve summing up all the entries 
			// and counting the number of entries.
			
			//*****************************************************************************************************************************
			// Question 1, 5, 6, and 7 data extraction, sum temperature of all 12 months for each year.
			
            int index = year - START_YEAR;
            yearly_sum[index] += temperature;
            yearly_count[index]++;      
            
            //*****************************************************************************************************************************
            // Question 2 data extraction, sum temperature of all 1200 months for each century.
            
            if (year >= 1760 && year <= 1799) { // 18th century
                century_sum[0] += temperature;
                century_count[0]++;
            } else if (year >= 1800 && year <= 1899) { // 19th century
                century_sum[1] += temperature;
                century_count[1]++;

            } else if (year >= 1900 && year <= 1999) { // 20th century
                century_sum[2] += temperature;
                century_count[2]++;
                
            } else if (year >= 2000 && year <= 2015) { // 21st century
                century_sum[3] += temperature;
                century_count[3]++;
			}
			
			//*****************************************************************************************************************************
			// Question 3 data extraction, sum temperature of each month for years from 1900-2015.
			
            int month_index = month - 1; // Months are 1-indexed, convert to 0-indexed
            if (year>= 1900 && year<= 2015){
				
				monthly_sum[month_index] += temperature;
            	monthly_count[month_index]++;
	}
			//*****************************************************************************************************************************
			// Question 4 data extraction, find hottest/coldest month and its year
			
            if (temperature > hottest_temperature) {
                hottest_temperature = temperature;
                strcpy(hottest_month, months[month_index]);
                hottest_year = year;
            }
            if (temperature < coldest_temperature) {
                coldest_temperature = temperature;
                strcpy(coldest_month, months[month_index]);
                coldest_year = year;
            }
            
			//*****************************************************************************************************************************
            // Question 8, 9, 11 data extraction.  
            
			int index2 = year - START_YEAR2;
            if (year>=1850 && year<= 2015){
				
            // q8
				yearly_sum_q8[index2] += temperature;
				yearly_sum_max_q8[index2] += temperature_max;
				yearly_sum_min_q8[index2] += temperature_min;
				yearly_count_q8[index2]++;
         
         
            // q9
            if (year >= 1800 && year <= 1899) { // 19th century
                century_sum_q9[0] += temperature;
                century_sum_max_q9[0] += temperature_max;
                century_sum_min_q9[0] += temperature_min;
                century_count_q9[0]++;
            } else if (year >= 1900 && year <= 1999) { // 20th century
                century_sum_q9[1] += temperature;
                century_sum_max_q9[1] += temperature_max;
                century_sum_min_q9[1] += temperature_min;
                century_count_q9[1]++;
            } else if (year >= 2000 && year <= 2015) { // 21st century
                century_sum_q9[2] += temperature;
                century_sum_max_q9[2] += temperature_max;
                century_sum_min_q9[2] += temperature_min;
                century_count_q9[2]++;
			}
			
            // q11			
				yearlyq11_sum[index2] += temperature;
				yearlyq11_count[index2]++;
				yearlyq11_sum_oce[index2] += temp_oce;
				yearlyq11_count_oce[index2]++;
			}
			
			//*****************************************************************************************************************************
			// Question 10 data extraction, sum temp and uncertainty for each month for years 2000-2015.
            if (year>=2000 && year<= 2015){
				monthlyq10_sum[month_index] += temperature;
				monthlyq10_count[month_index]++;
				q10_unc_sum[month_index] += uncertainty;
				q10_unc_count[month_index]++;
			}	
			
        
		}
	}
    fclose(GlobalTempsFile);
	
//*****************************************************************************************************************************
// QUESTION 1 CALCULATION AND OUTPUT TO FILE. (QUESTION 6 DATA)
// QUESTION 5 CALCULATION.
// QUESTION 7 EXTRACTION.
    FILE *yearly_file = fopen("yearly_averages.txt", "w");
    if (yearly_file == NULL) {
        fprintf(stderr, "Error opening yearly averages file.\n");
        return 1;
    }
    fprintf(yearly_file, "Year\tAverage Temperature\n");
    for (int i = 0; i < END_YEAR - START_YEAR + 1; i++) {
        if (yearly_count[i] > 0) {
			
			// QUESTION 1 CALCULATION
            float average_temperature = yearly_sum[i] / yearly_count[i];
            
			// QUESTION 7 EXTRACTION
			// Add avg temperature for each year to its corresponding century.
            if (1800<=(START_YEAR + i) && (START_YEAR + i) <= 1899){
				
				c_19[(START_YEAR + i)-1800] = average_temperature;	
			}
            if (1900<=(START_YEAR + i) && (START_YEAR + i) <= 1999){
				
				c_20[(START_YEAR + i)-1900] = average_temperature;	
			}
			
			// QUESTION 1 OUTPUT (WILL BE USED FOR QUESTION 6)
            fprintf(yearly_file, "%d\t%.2f\n", START_YEAR + i, average_temperature);
 
            // QUESTION 5 Track hottest and coldest years
            if (average_temperature > hottest_year_temp) {
                hottest_year_temp = average_temperature;
                hottest_year_recorded = START_YEAR + i;
            }
            if (average_temperature < coldest_year_temp) {
                coldest_year_temp = average_temperature;
                coldest_year_recorded = START_YEAR + i;
            }
        }
    }
    fclose(yearly_file);

//*****************************************************************************************************************************
// QUESTION 2 CALCULATION AND OUTPUT TO FILE.

    FILE *century_file = fopen("century_averages.txt", "w");
    if (century_file == NULL) {
        fprintf(stderr, "Error opening century averages file.\n");
        return 1;
    }
    fprintf(century_file, "Century\tAverage Temperature\n");
    for (int i = 0; i < 4; i++) {
        if (century_count[i] > 0) {
            float average_temperature = century_sum[i] / century_count[i];
            fprintf(century_file, "%dth\t%.2f\n", i + 18, average_temperature);
        }
    }
    fclose(century_file);
    
//*****************************************************************************************************************************
// QUESTION 3 CALCULATION AND OUTPUT TO FILE.

	FILE *monthly_file = fopen("monthly_averages.txt", "w");
    if (monthly_file == NULL) {
        fprintf(stderr, "Error opening century averages file.\n");
        return 1;
    }
    fprintf(monthly_file, "Month\tAverage Temperature\n");
    for (int i = 0; i < 12; i++) {
        if (monthly_count[i] > 0) {
            float average_temperature = monthly_sum[i] / monthly_count[i];
            fprintf(monthly_file, "%s\t%.2f\n", months[i], average_temperature);
        }
    }
    fclose(monthly_file);
    
//*****************************************************************************************************************************
// QUESTION 4 AND 5 OUTPUT TO USER.

// Output message but not actual output values for Q1,Q2,Q3.
	printf("Yearly, century, and monthly averages written to files successfully!\n");
	
// Q4
	printf("Hottest month: %s %d (Average Temperature: %.2f)\n", hottest_month, hottest_year, hottest_temperature);
    printf("Coldest month: %s %d (Average Temperature: %.2f)\n", coldest_month, coldest_year, coldest_temperature);
    
// Q5
    printf("Hottest year: %d (Average Temperature: %.2f)\n", hottest_year_recorded, hottest_year_temp);
    printf("Coldest year: %d (Average Temperature: %.2f)\n", coldest_year_recorded, coldest_year_temp);
    
//*****************************************************************************************************************************
// QUESTION 7 DATA OUTPUT TO FILE.

	FILE * century_19_20 = fopen("century_19_20.txt", "w");
	
	for (int i=0; i<100; i++){
		fprintf(century_19_20, "%d %lf %lf\n", i, c_19[i], c_20[i]);
	}
	
	fclose(century_19_20);
	
    
//*****************************************************************************************************************************
// QUESTION 8 CALCULATION AND OUTPUT TO FILE.

    FILE *yearly_q8__file = fopen("question_8_yearly_averages.txt", "w");
    if (yearly_q8__file == NULL) {
        fprintf(stderr, "Error opening yearly averages file.\n");
        return 1;
    }

    for (int i = 0; i < END_YEAR2 - START_YEAR2 + 1; i++) {
        if (yearly_count_q8[i] > 0) {
            float average_temperature_q8 = yearly_sum_q8[i] / yearly_count_q8[i];
            float average_temperature_max_q8 = yearly_sum_max_q8[i] / yearly_count_q8[i];
            float average_temperature_min_q8 = yearly_sum_min_q8[i] / yearly_count_q8[i];
            fprintf(yearly_q8__file, "%d\t%f\t%f\t%f\n", START_YEAR2 + i, average_temperature_q8, average_temperature_max_q8, average_temperature_min_q8);
        }
    }
    fclose(yearly_q8__file);
    
//*****************************************************************************************************************************
// QUESTION 9 CALCULATION AND OUTPUT TO FILE.
    FILE *question_9_data = fopen("question_9_data.txt", "w");
    if (question_9_data == NULL) {
        fprintf(stderr, "Error opening century averages file.\n");
        return 1;
    }
    for (int i = 0; i < 3; i++) {
        if (century_count_q9[i] > 0) {
            float average_temperature_q9 = century_sum_q9[i] / century_count_q9[i];
            float average_temperature_max_q9 = century_sum_max_q9[i] / century_count_q9[i];
            float average_temperature_min_q9 = century_sum_min_q9[i] / century_count_q9[i];
            fprintf(question_9_data, "%d\t%f\t%f\t%f\n", i + 19, average_temperature_q9, average_temperature_max_q9, average_temperature_min_q9);
        }
    }
    fclose(question_9_data);
 
//*****************************************************************************************************************************
// QUESTION 10 CALCULATION AND OUTPUT TO FILE.

    FILE *monthlyq10_file = fopen("monthlyq10_averages.txt", "w");
    if (monthlyq10_file == NULL) {
		fprintf(stderr, "Error opening monthlyq9 averages file.\n");
		return 1;
	}
	 for (int i = 0; i < 12; i++) {
        if (monthlyq10_count[i] > 0) {
            float average_temperature = monthlyq10_sum[i] / monthlyq10_count[i];
            float average_uncertainty = q10_unc_sum[i] / q10_unc_count[i];
            fprintf(monthlyq10_file, "%s\t%f\t%f\n", months[i], average_temperature, average_uncertainty);
        }
    }
    fclose(monthlyq10_file);
    
//*****************************************************************************************************************************
// QUESTION 11 CALCULATION AND OUTPUT TO FILE.
    
    FILE *yearlyq11_file = fopen("yearlyq11_averages.txt", "w");
    if (yearlyq11_file == NULL) {
        fprintf(stderr, "Error opening yearly averages file.\n");
        return 1;
    }
    for (int i = 0; i < END_YEAR2 - START_YEAR2 + 1; i++) {
        if (yearlyq11_count[i] > 0) {
            float average_temperature = yearlyq11_sum[i] / yearlyq11_count[i];
            float average_temperature_oce = yearlyq11_sum_oce[i] / yearlyq11_count[i];
    
            fprintf(yearlyq11_file, "%d\t%f\t%f\n", START_YEAR2 + i, average_temperature, average_temperature_oce);

        }
    }
    fclose(yearlyq11_file);
    
    return 0;
}

//*****************************************************************************************************************************
//*****************************************************************************************************************************
// END OF PROGRAM

