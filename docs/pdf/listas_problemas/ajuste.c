/* Programa ajuste.c
   Ajuste de curvas pelo metodo dos minimos quadrados
   Autor: Carlos Y. Shigue
   Tipos de ajuste: (1) linear	    : y = a + b*x
		    (2) exponencial : y = a*exp(b*x)
					(3) logaritmo	: y =  a +b*ln x
					(4) potencial	: y = a*x^b
					(5) hiperbolico : y = a + b/x
   Soma dos desvios quadraticos: S = soma{(y-yaj)^2}
   Coeficiente de correlacao: r^2 = 1 - n*S/{n*soma(y^2) - (soma(y))^2}
*/

#include <stdio.h>
#include <math.h>
#include <conio.h>

#define NPMAX	  500	  /* Numero maximo de pontos */

int npt;       /* Variavel de escopo global */

void main()
{
	void linear(float *, float *, float *, float [], float []);

	float x, y, dev, sqdev, r2;
	float coef;
	float a0, a1, a[5], b[5], r[5];
	float xx[NPMAX], yy[NPMAX], xlog[NPMAX], ylog[NPMAX], xinv[NPMAX];
	int i, k, flagx, flagxnull, flagy, repete;
	char entra[32];
	FILE *fid;

	/* Leitura do arquivo dos dados de entrada (x,y) */
    printf("Nome do arquivo: ");
	scanf("%s", entra);
	fid = fopen(entra, "r");
	if (fid == NULL) {
		printf("\nArquivo inexistente ou com nome errado\n");
		printf("Tecle <ENTER> para encerrar a execucao do programa\n");
		getch();
		exit(1);
	}
	flagx = 1;
	flagxnull = 1;
	flagy = 1;

	/* Verificacao da existencia de valores negativos ou nulos de x e y */
	while (!feof(fid)) {
		npt++;
		fscanf(fid, "%g %g", &x, &y);
		xx[npt] = x;
		yy[npt] = y;
		if (x <= 0) flagx = 0;
		if (x == 0) flagxnull = 0;
		if (y <= 0) flagy = 0;
	}
	fclose(fid);
	npt = npt - 1;

	printf("Numero de pontos = %d\n", npt);
	for (i = 1; i <= npt; i++)
		printf("x(%d) = %lf  y(%d) = %lf\n", i, xx[i], i, yy[i]);
	printf("\nTecle <ENTER> para continuar\n");
	getch();
	printf("\n\n Resultados dos ajustes\n\n");

	/* Calculo dos ajustes nao-lineares atraves de linearizacao */
	for (k = 1; k <= 5; k++) {

		switch(k) {

		   /* Ajuste linear */
		   case 1:
		      linear(&a0, &a1, &r2, xx, yy);
			  a[k] = a0;
			  b[k] = a1;
			  r[k] = r2;
			  printf(" Linear: y = %f ", a[k]);
		      if (b[k] > 0)
				  printf(" + %f*x\n", b[k]);
			  else
				  printf(" %f*x\n", b[k]);
			  printf(" Coeficiente de correlacao r2 = %f\n\n", r[k]);
			  break;

		   /* Ajuste exponencial */
		   case 2:
		      if (flagy == 0) {
				   printf("\nNao e possivel o ajuste exponencial. Valor de y negativo ou nulo.\n");
				   break;
				}
			  else {
				 for (i = 1; i <= npt; i++)
					 ylog[i] = log(yy[i]);
			 linear(&a0, &a1, &r2, xx, ylog);
				 a[k] = a0;
				 b[k] = a1;
				 r[k] = r2;
				 coef = exp(a[k]);
				 printf(" Exponencial: y = %lf*exp(%f*x)\n", coef, b[k]);
				 printf(" Coeficiente de correlacao r2 = %f\n\n", r[k]);
				 break;
			  }

		   /* Ajuste logartimo */
		   case 3:
			    if (flagx == 0) {
				   printf("\nNao e possivel o ajuste logaritmo. Valor de x negativo ou nulo.\n");
				   break;
				}
			    else {
				  for (i = 1; i <= npt; i++)
					  xlog[i] = log(xx[i]);
			      linear(&a0, &a1, &r2, xlog, yy);
				  a[k] = a0;
				  b[k] = a1;
				  r[k] = r2;
				  printf(" Logaritmo: y = %f ", a[k]);
			  if (b[k] > 0)
					printf(" + %f*ln(x)\n", b[k]);
				  else
					printf(" %f*ln(x)\n", b[k]);
				  printf(" Coeficiente de correlacao r2 = %f\n\n", r[k]);
				  break;
			    }

		   /* Ajuste potencial */
		   case 4:
			if (flagx == 0 || flagy == 0) {
				   printf("\nNao e possivel o ajuste potencial. Valor de x ou y negativo ou nulo.\n");
				   break;
				}
				else {
				  for (i = 1; i <= npt; i++) {
					xlog[i] = log(xx[i]);
					ylog[i] = log(yy[i]);
				  }
				  linear(&a0, &a1, &r2, xlog, ylog);
				  a[k] = a0;
				  b[k] = a1;
				  r[k] = r2;
				  coef = exp(a[k]);
				  printf(" Potencial: y = %lf*x^(%f)\n", coef, b[k]);
				  printf(" Coeficiente de correlacao r2 = %f\n\n", r[k]);
				  break;
			    }

		   /* Ajuste hiperbolico */
		   case 5:
			 if (flagxnull == 0) {
			       printf("\nNao e possivel o ajuste hiperbolico. Valor de x nulo.\n");
			       break;
			     }
			     else {
				   for (i = 1; i <= npt; i++)
				 xinv[i] = 1.0 / xx[i];
			   linear(&a0, &a1, &r2, xinv, yy);
				   a[k] = a0;
				   b[k] = a1;
				   r[k] = r2;
				   printf(" Hiperbolico: y = %f ", a[k]);
			   if (b[k] > 0)
				  printf(" + %f/x\n", b[k]);
				   else
				  printf(" %f/x\n", b[k]);
				   printf(" Coeficiente de correlacao r2 = %f\n\n", r[k]);
				}

		}

	}

	printf("\n\nExecucao do programa terminado. Tecle <ENTER> para encerrar ...\n");
	getch();
}

/* Calculo da solucao das equacoes normais para o ajuste linear */
void linear(float *a, float *b, float *rr, float x[], float y[])
{
	int i;
	float sumx = 0, sumy = 0, sumx2 = 0, sumxy = 0, sumy2 = 0;
    float S = 0, dev, sqdev;

	for (i = 1; i <= npt; i++) {
		sumx += x[i];
		sumy += y[i];
		sumx2 += x[i]*x[i];
		sumxy += x[i]*y[i];
	}

	*a = (sumx2*sumy - sumx*sumxy)/(npt*sumx2 - sumx*sumx);
	*b = (npt*sumxy - sumx*sumy)/(npt*sumx2 - sumx*sumx);

	for (i = 1; i <= npt; i++) {
		dev = y[i] - (*a + (*b)*x[i]);
		sqdev = pow(dev,2);
		S += sqdev;
		sumy2 +=  y[i]*y[i];
	}

	*rr = 1 - npt*S/(npt*sumy2 - sumy*sumy);
}
