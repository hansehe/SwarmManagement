from SwarmManagement import SwarmManager
import sys
import logging


def main():
    """Entry point for the application script"""
    arguments = sys.argv[1:]
    logging.basicConfig(level=logging.INFO)
    SwarmManager.HandleManagement(arguments)

if __name__ == "__main__":
    main()