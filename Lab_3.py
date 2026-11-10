# CIS-117 Lab3
# Reads country_full.csv and splits countries into separate CSV files by region.
# Mark Demot
import csv

def split_countries_by_region(input_filename):
    regions = {}

    try:
        with open(input_filename, mode ="r", encoding="utf-8", newline="" ) as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                country_name = row["Country"].strip()
                region_name = row["Region"].strip()

                if not country_name or not region_name:
                    continue

                if region_name not in regions:
                    regions[region_name] = []

                regions[region_name].append([country_name, region_name])

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'")
        return
    except IOError as e:
        print(f"I/O error occured while reading '{input_filename}': {e}")
        return
    except KeyError as e:
        print(f"Error: Missing expected column in CSV file: {e}")
        return

    for region, country_rows in regions.items():
        output_filename = f"{region.replace(' ', '_')}.csv"

        try:
            with open(output_filename, mode="w", encoding="utf-8", newline="") as outfile:
                writer = csv.writer(outfile)

                writer.writerow(["Country", "Region"])

                writer.writerows(country_rows)

            print(f"Successfully created '{output_filename}' with {len(country_rows)} countries.")

        except PermissionError:
            print(f"Error: Permission denied when trying to write '{output_filename}'.")
        except IOError as e:
            print(f"I/O error occured while writing '{output_filename}': {e}")

if __name__ == "__main__":
    split_countries_by_region("country_full.csv")



