#!/bin/bash
export SQLALCHEMY_SILENCE_UBER_WARNING=1

set -e # Exit if any command fails
echo "Replacing variables.."
bash scripts/replace_variables.bash
echo "Done replacing variables.."

echo "Running data validate..."
bash scripts/validate-data.bash
echo "Done validating data."

echo "Starting to train..."
bash scripts/train.bash
echo "Done training."

echo "Starting tests..."
bash scripts/test.bash
echo "Testing done."

echo "Failed stories: "
cat results/failed_test_stories.yml
echo -e "\nStories with warnings: "
cat results/stories_with_warnings.yml
# echo ""

echo "Removing variables and cleaning data.."
bash scripts/replace_templates.bash
echo "Done removing variable and cleaning data."
echo ""