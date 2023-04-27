#
# PySNMP MIB module STORMSHIELD-AUTHUSERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTHUSERS-MIB
# Produced by pysmi-1.1.8 at Thu Apr 27 10:35:08 2023
# On host fv-az842-726 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ObjectIdentity, IpAddress, MibIdentifier, Counter32, TimeTicks, NotificationType, iso, Counter64, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "TimeTicks", "NotificationType", "iso", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("STORMSHIELD-AUTHUSERS-MIB", snsAuthUsersDomain=snsAuthUsersDomain, snsAuthUsersEntry=snsAuthUsersEntry, snsAuthUsersTimeOut=snsAuthUsersTimeOut, snsAuthUsersIPAddr=snsAuthUsersIPAddr, PYSNMP_MODULE_ID=snsUsers, snsUsers=snsUsers, snsAuthUsersTable=snsAuthUsersTable, snsAuthUsersName=snsAuthUsersName)
