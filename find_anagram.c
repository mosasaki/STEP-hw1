

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define SIZE 72412
#define LINE_LENGTH 20
#define NOT_FOUND (-1)

int n;

typedef struct Dictionary{
    char *original;
    char *sorted;
}Dictionary;

Dictionary table[SIZE];


void insert_end(char *orig, char *sort);
void table_quicksort(Dictionary table[], int left, int right);
void read_file(char *filename);
void sort(char *quickorig, int left, int right);
char *quicksort(char *orig, int left, int right);
char *find_anagram(char *input);



void insert_end(char *orig, char *sort){
    table[n].original = orig;
    table[n].sorted = sort;
    n++;
}


void sort(char *quickorig,int left,int right){
    int pivot,i,j,tmp;

    if(left < right){
        pivot = quickorig[left];
        i = left;
        j = right;
        while(i <j ){

            while(quickorig[i] < pivot){
                i++;
            }
            while(quickorig[j] > pivot){
                j--;
            }
            if(i <= j ){
                tmp = quickorig[i];
                quickorig[i] = quickorig[j];
                quickorig[j] = tmp;
                i++;
                j--;
            }
        }
        sort(quickorig, left, j);
        sort(quickorig, i, right);
    }
}

char *quicksort(char *orig,int left,int right){
    char *quickorig;
    quickorig = (char *) malloc (LINE_LENGTH);
    strcpy(quickorig,orig);


    sort(quickorig,left,right);
    return(quickorig);

}


void table_quicksort(Dictionary table[], int left, int right) {

int i,j;
char *pivot;
Dictionary tmp;

if(left < right) {
    i = left;
    j = right;
    pivot = table[(left + right) / 2].sorted;

    while(i < j){
        while(strcasecmp(table[i].sorted, pivot)<0){
            i++;
        }
        while(strcasecmp(table[j].sorted, pivot) > 0){
            j--;
        }
        if(i <= j){
            tmp.original = table[i].original;
            tmp.sorted = table[i].sorted;
            table[i].original = table[j].original;
            table[i].sorted = table[j].sorted;
            table[j].original = tmp.original;
            table[j].sorted = tmp.sorted;
            i++;
            j--;
        }
    }
    table_quicksort(table,left,j);
    table_quicksort(table,i,right);
}

}

void read_file(char *filename){
    FILE *file;
    char *original, *sorted;

    int r;

    file = fopen(filename,"r");
    if(file == NULL){
        printf("Cannot find %s\n",filename);
        exit(1);
    }

    while(1){
        original = (char *) malloc (LINE_LENGTH);
        r = fscanf(file, "%s\n", original);

        if(r == EOF){
            fclose(file);
            return;
        }
        else {
            sorted = quicksort(original,0,strlen(original)-1);
            insert_end(original,sorted);
            //printf("TEST after insert_end %s,%s\n",original,sorted);
        }
    }

}



char *find_anagram(char *input){
    int lo,hi,mid;

    input = quicksort(input,0,strlen(input)-1);
    //printf("TEST AFTER input sort %s \n",input);

    lo = 0;
    hi = SIZE-1;

    while(lo <= hi){

        mid =(lo + hi)/2;
        if(strcasecmp(input,table[mid].sorted)==0){
            return table[mid].original;
        }
        else if(strcasecmp(input,table[mid].sorted) > 0){
            lo = mid + 1;
        }
        else{
            hi = mid - 1;
        }

    }
    return "could not find anagram";

}




int main(void){
    char *input, *result;
   
    n = 0;
    int i = 0;

    read_file("dictionary.words");
    //printf("TEST after read_file %s\n",table[0].sorted);

    table_quicksort(table,0,SIZE-1);
    //printf("TEST AFTER table_sort \n");


    while(i<10) {
        printf("Enter:");
        scanf("%s", input);

        result = find_anagram(input);
        printf("%s\n", result);
        i++;
    }
        return 0;

}

