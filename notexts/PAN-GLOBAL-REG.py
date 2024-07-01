#
# PySNMP MIB module PAN-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-REG-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:23:45 2024
# On host fv-az735-465 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, iso, Counter32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, Bits, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "iso", "Counter32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 1))
panGlobalRegModule.setRevisions(('2011-02-09 16:10',))
if mibBuilder.loadTexts: panGlobalRegModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalRegModule.setOrganization('Palo Alto Networks')
panRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461))
if mibBuilder.loadTexts: panRoot.setStatus('current')
panReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1))
if mibBuilder.loadTexts: panReg.setStatus('current')
panModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1))
if mibBuilder.loadTexts: panModules.setStatus('current')
panMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2))
if mibBuilder.loadTexts: panMibs.setStatus('current')
panCommonMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 1))
if mibBuilder.loadTexts: panCommonMib.setStatus('current')
panSpecificMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 2))
if mibBuilder.loadTexts: panSpecificMib.setStatus('current')
panProductsMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3))
if mibBuilder.loadTexts: panProductsMibs.setStatus('current')
mibBuilder.exportSymbols("PAN-GLOBAL-REG", panGlobalRegModule=panGlobalRegModule, panProductsMibs=panProductsMibs, panRoot=panRoot, PYSNMP_MODULE_ID=panGlobalRegModule, panMibs=panMibs, panCommonMib=panCommonMib, panModules=panModules, panSpecificMib=panSpecificMib, panReg=panReg)
