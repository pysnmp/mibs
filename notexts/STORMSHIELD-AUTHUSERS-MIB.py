#
# PySNMP MIB module STORMSHIELD-AUTHUSERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTHUSERS-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:12:13 2024
# On host fv-az1490-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, ModuleIdentity, Unsigned32, Integer32, iso, TimeTicks, Gauge32, NotificationType, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32", "iso", "TimeTicks", "Gauge32", "NotificationType", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32")
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
mibBuilder.exportSymbols("STORMSHIELD-AUTHUSERS-MIB", snsAuthUsersEntry=snsAuthUsersEntry, snsAuthUsersName=snsAuthUsersName, snsUsers=snsUsers, PYSNMP_MODULE_ID=snsUsers, snsAuthUsersIPAddr=snsAuthUsersIPAddr, snsAuthUsersTable=snsAuthUsersTable, snsAuthUsersTimeOut=snsAuthUsersTimeOut, snsAuthUsersDomain=snsAuthUsersDomain)
