#
# PySNMP MIB module STORMSHIELD-AUTHUSERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTHUSERS-MIB
# Produced by pysmi-1.1.8 at Fri Sep  8 08:10:48 2023
# On host fv-az256-323 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Bits, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Unsigned32, iso, Counter64, ObjectIdentity, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Bits", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Unsigned32", "iso", "Counter64", "ObjectIdentity", "Gauge32", "ModuleIdentity")
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
mibBuilder.exportSymbols("STORMSHIELD-AUTHUSERS-MIB", snsAuthUsersDomain=snsAuthUsersDomain, snsAuthUsersEntry=snsAuthUsersEntry, snsAuthUsersName=snsAuthUsersName, PYSNMP_MODULE_ID=snsUsers, snsAuthUsersTimeOut=snsAuthUsersTimeOut, snsAuthUsersIPAddr=snsAuthUsersIPAddr, snsUsers=snsUsers, snsAuthUsersTable=snsAuthUsersTable)
