namespace prueba_tecnica_datamart
{
    /// <summary>
    /// Prueba Técnica - Backend Developer - Datamart
    /// Aspirante: Santiago Esteawens Torres Zapata
    /// </summary>
    public class Program
    {
        /// <summary>
        /// 4. Escribe una función llamada isAnagram que acepte dos cadenas de texto como parámetros y 
        /// determine si son anagramas (es decir, si tienen exactamente las mismas letras, pero en diferente orden).
        /// </summary>
        /// <param name="string1">cadena de texto 1 a evaluar</param>
        /// <param name="string2">cadena de texto 2 a evaluar</param>
        /// <returns>resultado boleano, True o False</returns>
        public static bool IsAnagram(string string1, string string2)
        {
            if (string1.Length != string2.Length)
            {
                return false;
            }

            // Convierte ambas cadenas de string a minusculas y ordena cada caracter
            char[] characters1 = [.. string1.ToLower().OrderBy(c => c)];
            char[] characters2 = [.. string2.ToLower().OrderBy(c => c)];

            // Compara los caracteres ordenados
            for (int i = 0; i < characters1.Length; i++)
            {
                if (characters1[i] != characters2[i])
                {
                    return false;
                }
            }

            return true;
        }

        /// <summary>
        /// 5. Escribe una función llamada findCommonElements que acepte una lista de listas como parámetro
        /// y devuelva una lista con los elementos comunes a todas las sub-listas.
        /// </summary>
        /// <typeparam name="T">lista generica</typeparam>
        /// <param name="lists">lista de listas</param>
        /// <returns>lista con elementos comunes</returns>
        public static List<T> FindCommonElements<T>(List<List<T>> lists)
        {
            if (lists == null || lists.Count == 0)
            {
                return [];
            }

            HashSet<T> commonElements = new(lists[0]);
            for (int i = 1; i < lists.Count; i++)
            {
                commonElements.IntersectWith(lists[i]);
            }

            return [.. commonElements];
        }

        /// <summary>
        /// Escribe una implementación para el algoritmo de ordenamiento mergesort.
        /// </summary>
        /// <param name="array">Array para comparar</param>
        /// <param name="left">elemento a la izquierda</param>
        /// <param name="right">elemento a la derecha</param>
        public static void MergeSort(int[] array, int left, int right)
        {
            if (left < right)
            {
                int middle = (left + right) / 2;

                MergeSort(array, left, middle);
                MergeSort(array, middle + 1, right);

                Merge(array, left, middle, right);
            }
        }

        /// <summary>
        /// Escribe una implementación para el algoritmo de ordenamiento mergesort.
        /// </summary>
        /// <param name="array">Array para comparar</param>
        /// <param name="left">elemento a la izquierda</param>
        /// <param name="middle">elemento medio</param>
        /// <param name="right">elemento a la derecha</param>
        public static void Merge(int[] array, int left, int middle, int right)
        {
            int[] leftArray = new int[middle - left + 1];
            int[] rightArray = new int[right - middle];

            Array.Copy(array, left, leftArray, 0, middle - left + 1);
            Array.Copy(array, middle + 1, rightArray, 0, right - middle);

            int i = 0;
            int j = 0;
            for (int k = left; k < right + 1; k++)
            {
                if (i == leftArray.Length)
                {
                    array[k] = rightArray[j];
                    j++;
                }
                else if (j == rightArray.Length)
                {
                    array[k] = leftArray[i];
                    i++;
                }
                else if (leftArray[i] <= rightArray[j])
                {
                    array[k] = leftArray[i];
                    i++;
                }
                else
                {
                    array[k] = rightArray[j];
                    j++;
                }
            }
        }

        public static void Main()
        {
            Console.WriteLine("Problema 4.");
            string palabra1 = "anagram";
            string palabra2 = "nagaram";
            Console.WriteLine("Comprueba que las palabras " + palabra1 + " y " + palabra2 + " sean anagramas. " + IsAnagram(palabra1, palabra2));
            palabra1 = "rat";
            palabra2 = "car";
            Console.WriteLine("Comprueba que las palabras " + palabra1 + " y " + palabra2 + " sean anagramas. " + IsAnagram(palabra1, palabra2));

            Console.WriteLine("Problema 5.");
            List<List<int>> lists = [
                                        [1, 2, 3, 4, 5],
                                        [2, 3, 5, 7, 11],
                                        [1, 2, 3, 5, 8]
                                    ];

            List<int> commonElements = FindCommonElements(lists);
            Console.WriteLine("Resultado: " + string.Join(", ", commonElements));

            Console.WriteLine("Problema 6.");
            int[] array = [45, 32, 12, 77, 7, 23, 91];
            Console.WriteLine("Array antes de ordenar: " + string.Join(", ", array));

            MergeSort(array, 0, array.Length - 1);

            Console.WriteLine("Array después de ordenar: " + string.Join(", ", array));
        }
    }
}