#
# PySNMP MIB module STORMSHIELD-AUTHUSERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTHUSERS-MIB
# Produced by pysmi-1.1.12 at Wed Dec  4 17:59:51 2024
# On host fv-az2036-124 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, TimeTicks, ModuleIdentity, Bits, NotificationType, Gauge32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "TimeTicks", "ModuleIdentity", "Bits", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsUsers = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 2))
snsUsers.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsUsers.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsUsers.setOrganization('Stormshield')
snsAuthUsersTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1), )
if mibBuilder.loadTexts: snsAuthUsersTable.setStatus('current')
snsAuthUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1), ).setIndexNames((0, "STORMSHIELD-AUTHUSERS-MIB", "snsAuthUsersIPAddr"))
if mibBuilder.loadTexts: snsAuthUsersEntry.setStatus('current')
snsAuthUsersIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersIPAddr.setStatus('current')
snsAuthUsersTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersTimeOut.setStatus('current')
snsAuthUsersName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersName.setStatus('current')
snsAuthUsersDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAuthUsersDomain.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-AUTHUSERS-MIB", snsAuthUsersTable=snsAuthUsersTable, snsAuthUsersTimeOut=snsAuthUsersTimeOut, snsAuthUsersDomain=snsAuthUsersDomain, snsAuthUsersName=snsAuthUsersName, PYSNMP_MODULE_ID=snsUsers, snsAuthUsersIPAddr=snsAuthUsersIPAddr, snsAuthUsersEntry=snsAuthUsersEntry, snsUsers=snsUsers)
