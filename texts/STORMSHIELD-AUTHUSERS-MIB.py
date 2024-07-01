#
# PySNMP MIB module STORMSHIELD-AUTHUSERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTHUSERS-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:18:17 2024
# On host fv-az532-988 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, TimeTicks, Counter32, IpAddress, Gauge32, MibIdentifier, Bits, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "Counter32", "IpAddress", "Gauge32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsUsers = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 2))
snsUsers.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsUsers.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsUsers.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsUsers.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsUsers.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsUsers.setDescription('stormshield users MIBS')
snsAuthUsersTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1), )
if mibBuilder.loadTexts: snsAuthUsersTable.setStatus('current')
if mibBuilder.loadTexts: snsAuthUsersTable.setDescription('List of authentified users')
snsAuthUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1), ).setIndexNames((0, "STORMSHIELD-AUTHUSERS-MIB", "snsAuthUsersIPAddr"))
if mibBuilder.loadTexts: snsAuthUsersEntry.setStatus('current')
if mibBuilder.loadTexts: snsAuthUsersEntry.setDescription('Each entry in the snsAuthUsersTable holds a set of information\n         (IP, username, and timeout).')
snsAuthUsersIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersIPAddr.setStatus('current')
if mibBuilder.loadTexts: snsAuthUsersIPAddr.setDescription('IP address of the authenticated user')
snsAuthUsersTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersTimeOut.setStatus('current')
if mibBuilder.loadTexts: snsAuthUsersTimeOut.setDescription('Timeout')
snsAuthUsersName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersName.setStatus('current')
if mibBuilder.loadTexts: snsAuthUsersName.setDescription('Username')
snsAuthUsersDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersDomain.setStatus('current')
if mibBuilder.loadTexts: snsAuthUsersDomain.setDescription('Domain name')
mibBuilder.exportSymbols("STORMSHIELD-AUTHUSERS-MIB", snsAuthUsersTable=snsAuthUsersTable, snsAuthUsersEntry=snsAuthUsersEntry, PYSNMP_MODULE_ID=snsUsers, snsUsers=snsUsers, snsAuthUsersIPAddr=snsAuthUsersIPAddr, snsAuthUsersTimeOut=snsAuthUsersTimeOut, snsAuthUsersName=snsAuthUsersName, snsAuthUsersDomain=snsAuthUsersDomain)
