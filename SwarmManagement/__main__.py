from SwarmManagement import SwarmManager
import sys
import logging


def main():
    """Entry point for the application script"""
    arguments = sys.argv[1:]
    SwarmManager.HandleManagement(arguments)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()