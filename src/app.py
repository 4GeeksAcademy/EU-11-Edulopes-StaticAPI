from flask import Flask, request, jsonify
from datastructures import Family

app = Flask(__name__)
family = Family()
family.initialize_with_initial_members() 

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(family.get_all_members())

@app.route('/member', methods=['POST'])
def add_member():
    data = request.json
    family.add_member(data)
    return jsonify(data), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = family.get_member_by_id(id) 
    if member:
        return jsonify(member)
    return jsonify({"error": "Member not found"}), 404

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    success = family.delete_member(id)
    if success:
        return jsonify({"done": True})
    return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run()