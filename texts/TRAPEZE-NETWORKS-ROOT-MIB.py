#
# PySNMP MIB module TRAPEZE-NETWORKS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/TRAPEZE-NETWORKS-ROOT-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:32:21 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, iso, Counter32, enterprises, Counter64, ObjectIdentity, Bits, MibIdentifier, IpAddress, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "iso", "Counter32", "enterprises", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "IpAddress", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzRootMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525))
trpzRootMib.setRevisions(('2008-05-22 00:08', '2007-11-28 00:07', '2006-04-14 00:06', '2005-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzRootMib.setRevisionsDescriptions(('v3.1.1: Changed IMPORT of enterprises\n                from RFC1155-SMI to SNMPv2-SMI\n                (this will be published in 7.0 release)', 'v3.0.0: Added subtree for\n                wireless Management Applications specific MIBs\n                (this will be published in 7.0 release)', 'v2.0.5: Revised for 4.1 release', 'v1: initial version, as for 4.0 and older releases',))
if mibBuilder.loadTexts: trpzRootMib.setLastUpdated('200805220008Z')
if mibBuilder.loadTexts: trpzRootMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzRootMib.setContactInfo('Trapeze Networks Technical Support\n\t www.trapezenetworks.com\n\t US:            866.TRPZ.TAC\n\t International: 925.474.2400\n\t support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzRootMib.setDescription("Trapeze Networks Root MIB\n\n\tCopyright 2008 Trapeze Networks, Inc.\n\tAll rights reserved.\n\tThis Trapeze Networks SNMP Management Information Base\n\tSpecification (Specification) embodies Trapeze Networks'\n\tconfidential and proprietary intellectual property.\n\tTrapeze Networks retains all title and ownership in\n\tthe Specification, including any revisions.\n\n\tThis Specification is supplied 'AS IS' and Trapeze Networks\n\tmakes no warranty, either express or implied, as to the use,\n\toperation, condition, or performance of the Specification.")
trpzProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 1))
trpzTemporary = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 2))
trpzRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3))
trpzMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4))
trpzTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 5))
trpzMgmtAppMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 6))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-ROOT-MIB", trpzTraps=trpzTraps, trpzTemporary=trpzTemporary, trpzRegistration=trpzRegistration, trpzProducts=trpzProducts, PYSNMP_MODULE_ID=trpzRootMib, trpzMibs=trpzMibs, trpzRootMib=trpzRootMib, trpzMgmtAppMibs=trpzMgmtAppMibs)
